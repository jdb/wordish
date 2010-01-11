#!/usr/bin/env python
"""
Wordish allows to check the correctness of text files dpeicting on shell
operations about correctness. Several operations are efficiently
handled with a shell, other do not really have an alternative but have
no easy way to be checked or tested for regression.

- filesystems (formatting, raid, snapshotting)

- source version control,

- packaging,

- network, firewall or load balancing

Wordish is a project which aims at reconstructing a shell session
composed of commands and outputs, from a text file, then execute the
commands in a shell and compare the output of the command to the
output parsed from the text file.

"""



        #  option -v should switch on the report, no -v should just report errors


        #  must work with jdb's lvm article
        #  must be hooked to the sourcecode directive standalone, sphix and docutils


        # python -m wordish --test should show something
        # python -m wordish simple_session.txt should show something
        # python -m unittest -v wordish test_wordish should show something


from subprocess import Popen, STDOUT, PIPE
from shlex import shlex 
from itertools import takewhile
from StringIO import StringIO

class ShellSessionParser( object ):
    """
    An iterator which parses a text file of a shell session and yields
    pairs of commands and outputs
    
    >>> sess = ShellSessionParser( s="~$ (echo coucou\n) # hello\ncoucou" )
    >>> for c,o in sess: print c,o
    ...
    (echo coucou
    )
    coucou
    """

    # TODO: configurable prompt

    def __init__( self, f=None, s=None ):
        """
        The constructor takes a filename or an open file or a string
        as the shell session.

        The constructor sets the :attr:`tokens` member attribute with
        a shlex token stream initialised with the correct options for
        parsing comments and whitespace.
        """

        
        f = s if ( s is not None and f is None ) else f

        self.tokens = shlex( f if hasattr(f, "read") else file( f ) )

        self.tokens.commenters = '' 
        # deactivate shlex comments facility which won't work for us.
        # The terminating linefeed means two things: end of comment an
        # end of command. As shlex consume the terminating linefeed,
        # there is no end of command left.

        self.tokens.whitespace = ''
        # deactivate shlex whitespace munging. characters cited in
        # ``shlex.whitespace`` are not returned by get_token. If
        # empty, whitespaces are returned as they are which is what we
        # want: they definitely count in bash, and may count in
        # output, so we just want to keep them as theyr are.

        # overall, I am not sure I use shlex a lot...
        
        self.nested = 0

    def has_token( self ):
        """
        Return True when there are still tokens available, False if
        the stream token is empty.

        >>> sess = ShellSessionParser( s="~$ env | grep USER\nUSER=jd" ))
        >>> sess.has_token()
        True
        >>> for t in sess.tokens: pass
        >>> sesssion.has_token()
        False
        """
        t = self.tokens.get_token()
        return False if t==self.tokens.eof else self.tokens.push_token( t ) or True

    def end_of_output( self, token ):
        """
        Returns true if the token is after the last token of the
        output of a command, else returns false. The functions stops
        right before the prompt which can be either '~# ' or '~$ '.

        >>> sess = ShellSessionParser( s="youpi\n~# " )
        >>> sess.tokens.next()
        youpi
        >>> sess.end_of_output( 'youpi' )
        False
        >>> sess.tokens.next()
        '~'
        >>> sess.end_of_output( '~' )
        True
        """
        # TODO: in the unittest, make sure '~' occurs in the -1, -2, and -3 position.
        # also  make sure it occurs in the three last position at the same time.

        if token=='~':
            n1, n2 = [ self.tokens.next(), self.tokens.next() ]
            if n1 in '$#' and n2 == ' ':
                return True
            else:
                self.tokens.push_token( n1 ) 
                self.tokens.push_token( n2 )
                return False
        else:
            return False

    def end_of_command( self, token ):
        """
        Returns true if the token is after the last token of a command
        in the section, else returns false. The functions stops right
        before the linefeed but only when the linefeed is not nested in
        brackets or parenthesis.

        >>> sess = session( s="date\n" )
        >>> sess.tokens.next()
        date
        >>> sess.end_of_output( 'date' )
        False
        >>> sess.tokens.next()
        '\n'
        >>> sess.end_of_output( '\n' )
        True

        This is the end of output, since the linefeed was not nested.

        >>> sess = ShellSessionParser( s="(youpi\n)\n" )
        >>> [ sess.tokens.next() for i in range(3) ]
        [ '(', 'youpi', '\n' ]
        >>> sess.end_of_output( '\n' )
        False
        >>> sess.tokens.next(); sess.end_of_output( '\n' )
        '\n'
        True
        
        The first linefeed was nested in a subshell, hence was
        not the end of a command. The second linefedd was.
        """

        if token == '\n' or token == '#':
            if token=='#': 
                list( takewhile( lambda t:t!='\n', self.tokens ) )
                token = '\n'
	
                if self.nested==0:
                    return True
        else:

            if   token in '({': self.nested += 1
            elif token in '})': self.nested -= 1

            return False

    def take_until( self, is_output=False ):
        """
        Returns a command or an output depending of the terminator
        provided. i.e. every token on which the terminator returns
        False. The terminator is a function which take a token and
        returns whether the stream of tokens is terminated or not.

        >>> session = ShellSessionParser
        >>> session( s="cmd" ).take_until()
        cmd
        >>> session( s="t () {\ncmd\n)\nhello" ).take_until()
        t () {
        cmd
        }

        Let's see with the output of the command:

        >>> session( s="t () {\ncmd\n)\nhello" ).take_until()
        
        """
        
        terminator = self.end_of_output if is_output else self.end_of_command

        return ''.join (
            [ t for t in self.tokens if not terminator( t ) ]
            ).strip()
            

    def __iter__(self):
        return self

    def next(self):
        """
        Returns the next pair of command and output.

        TODO: some unittest on the corner cases: empty file, only command, only outputs

        >>> session = ShellSession
        >>> sess = session( s="~# cmd1\noutput1\n~# cmd2\n" )
        >>> for c,o in sess: print "command: %s\noutput: %o" % (c,o)
        command: cmd
        output: output
        command: true
        output: 
        """

        self.take_until( self.end_of_output ) 

        while self.has_token() :
            return ( self.take_until( self.end_of_command ), 
                     self.take_until( self.end_of_output ) ) 
        else:
            raise StopIteration


def lex ( s, shlex_object=False, com='', whi='' ):
    """
    Debug function: returns the list of tokens of the input string.

    The token commenters and whitespace are set to the empty string
    and can be modified with the function arguments 'com' and
    'whi'. 

    If the argument shlex_object is set to True then it'is not the
    list of tokens but the shlex object itself so that you can
    experiment with the :obj:`shlex` and it multiple attribute and
    method.

    >>> lex( "Yozza 1 2" )
    ['Yozza', ' ', '1', ' ', '2']

    >>> tokens = lex( "Yozza 1 2", shlex_object=True )
    >>> tokens.whitespace = ' '
    >>> [t for t in tokens ]
    ['Yozza', '1', '2']

    >>>> lex( "Yozza # a comment you dont want to see", whi=' ', com='#' )
    ['Yozza']
    """

    tokens = shlex( StringIO( s )) 
    tokens.commenters = com         
    tokens.whitespace = whi         

    if shlex_object:
        return tokens
    else:
        return list( tokens )


class CommandRunner ( object ):
    """
    Implements a python "context manager", when entering the context,
    create a shell in a subprocess, the call method takes a string
    with a shell command and execute it in the shell. call ret output of the command.

    >>> with CommandRunner() as sh:
    ...    sh.call("echo coucou")
    ...    sh.call("a=$((1+1))")
    ...    sh.call("echo $a")
    ...
    coucou
    2
    """

    stderr_on_stdout = True

    def __enter__(self ):
        self.stderr_dir = STDOUT if CommandRunner.stderr_on_stdout else PIPE

        self.shell = Popen( "sh", shell=True, stdin=PIPE, stdout=PIPE, stderr=self.stderr_dir )
        self.stdout_tokens = ShellSessionParser(self.shell.stdout)
        return self

    def call(self, cmd):
        """in it and sends it to the shell via stdin. Then, stdout is
        read until a prompt following a linefeed. The prompt is
        suppressed and the tokens read are joined and returned as
        the"""

        # TODO: set the returncode, get stderr if needed, use the CommandOutput: 
        # TODO: set the ellipsis

        self.shell.stdin.write(cmd + '\necho "~$ "\n')
        return self.stdout_tokens.get_output()
        
    def __exit__(self, *arg):
        self.p.terminate()
        # If the child shell is hanged, maybe self.p.send_signal( signal.SIGKILL )
        # is more robust


class CommandOutput( object ):

    # should return a namedtuple out, err and returncode whose equald
    # is configurable ellipsis=...  the matching object has out, err,
    # returncode and an equal method which takes in account, stderr,
    # stdout and returncode if set. It should be possible to check
    # that return code is fine without bothering with the output. This
    # equald should also match against a simple string.

    # TODO: some docstrings
    # stdout for __repr__ and __str__

    def __init__(self, out=None, err=None, returncode=None, cmd=None ):
        self.out, self.err, self.returncode = out, err, returncode
        self.cmd = cmd

    def __str__(self):
        return self.out
    
    __repr__ = __str__
        
    def __neq__(self, other ):
        return not self.__eq__(other)

    def __eq__(self, other ):
        attrs = "out", "err", "returncode"
        other=CommandOutput(other) if isinstance(other, basestring) else other

        if not all( [ hasattr( other, a ) for a in attrs ]):
            raise TypeError("equality: argument must either a string or a CommandOutput instance.")
        
        return all( [ self.check(a) for a in attrs if a is not None ] )

    def check(self,other,member):
        if getattr(self, member) is not None and getattr(other, member) is not None:
            return getattr(self, member)==getattr(self, member)
        else: return None

    def exited_gracefully(self):
        return self.returncode==0

# TODO: design the correct object for the report formatter

def format_error(command, expected_output, output):
    return  "\n%s\nFailed example:\n\t%s\nExpected:\n\t%s\nGot:\n\t%s\n%s" % (
        '*' * 68, command, expected_output, output, '*' * 68)

if __name__=="__main__":

    import sys

    # TODO: make a man page a README file, in the egg place a test file for each
    # use case, raid, lvm, firewalling, load balancing, packaging, source version control 
    
    files = sys.argv[1:] if len( sys.argv ) > 1 else StringIO("""
~$ echo toto
toto

~$ echo $((1+1))
2

~$ echo "yozzza"
yozzza

~$ echo Youpi # what's up
Youpi

~$ echo "'~$'"
'~$'

~$ echo Yo # ~$
Yo

~$ echo $((1+1))
2

~$ echo $((1+2))
2

~$ lesbronzesfontduski # ~$
Yo
""")

    from wordish import ShellSessionParser
    from StringIO import StringIO

#     checker = OutputChecker()
#     for f in files:
#         with CommandRunner() as shell:
#             for c, o in ShellSessionParser( f ):
#                 if checker.add_output( shell.call( c ), o) == checker.crashed
#                     print checker.report()
#                     print( "Something broke, I am bailing out, you get to keep both pieces.")
#                     break
#     else:
#         print checker.report()



                
