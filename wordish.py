#!/usr/bin/env python
"""
Wordish is a project which aims at reconstructing a shell session
composed of commands and outputs, from a text file, then execute the
commands in a shell and compare the output of the command to the
output parsed from the text file.

Shell operations are easy to document, and with wordish, articles
including shell operations can be easily tested for correctness,
regression or compatibility on a particular system.

Areas of interest include filesystems operations, raid setup, volume
snapshots. Another area where wordish can be useful is in source
version control tutorial, or software packaging. Network setup,
firewall administration and load balancing tweaks are another examples
of operations usually carried out with a shell.
"""



        #  option -v should switch on the report, no -v should just report errors


        #  must work with jdb's lvm article
        #  must be hooked to the sourcecode directive standalone, sphix and docutils


        # python -m wordish --test should show something
        # python -m wordish simple_session.txt should show something
        # python -m unittest -v wordish test_wordish should show something


from subprocess import Popen, STDOUT, PIPE
from shlex import shlex 
from itertools import takewhile, chain
from StringIO import StringIO

class ShellSessionParser( object ):
    r"""
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
        f = StringIO(s) if ( s is not None and f is None ) else f

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
        r"""
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

    def is_output( self, token ):
        r"""
        Returns true if the token is after the last token of the
        output of a command, else returns false. The functions stops
        right before the prompt which can be either '~# ' or '~$ '.

        >>> sess = ShellSessionParser( s="youpi\n~# " )
        >>> sess.tokens.next()
        youpi
        >>> sess.is_output( 'youpi' )
        False
        >>> sess.tokens.next()
        '~'
        >>> sess.is_output( '~' )
        True
        """
        # TODO: in the unittest, make sure '~' occurs in the -1, -2, and -3 position.
        # also  make sure it occurs in the three last position at the same time.

        if token=='~':
            n1, n2 = [ self.tokens.next(), self.tokens.next() ]
            if n1 in '$#' and n2 == ' ':
                return False
            else:
                self.tokens.push_token( n2 ) 
                self.tokens.push_token( n1 )
                return True
        else:
            return True

    def is_command( self, token ):
        r"""
        Returns true if the token is after the last token of a command
        in the section, else returns false. The functions stops right
        before the linefeed but only when the linefeed is not nested in
        brackets or parenthesis.

        >>> sess = session( s="date\n" )
        >>> sess.tokens.next()
        date
        >>> sess.is_output( 'date' )
        False
        >>> sess.tokens.next()
        '\n'
        >>> sess.is_output( '\n' )
        True

        This is the end of output, since the linefeed was not nested.

        >>> sess = ShellSessionParser( s="(youpi\n)\n" )
        >>> [ sess.tokens.next() for i in range(3) ]
        [ '(', 'youpi', '\n' ]
        >>> sess.is_output( '\n' )
        False
        >>> sess.tokens.next(); sess.is_output( '\n' )
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
                return False
        else:

            if   token in '({': self.nested += 1
            elif token in '})': self.nested -= 1

        return True

    def takewhile( self, is_output=False ):
        r"""
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
        return ''.join (
            list( takewhile(
                    self.is_output if is_output else self.is_command, 
                    self.tokens )
                 ) ).strip()
            
    def __iter__(self):
        r"""
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
        self.takewhile( is_output=True ) 
        while self.has_token() :
            yield self.takewhile(), self.takewhile( is_output=True )


    
    def toscript(self):
        commentize = lambda o: '#%s\n' % o.replace( '\n', '\n#' )
        return "#!/bin/sh\nset -e -x\n" + '\n'.join(  
            chain( *( ( c, commentize(o) ) for c, o in self ) ) )
            

def lex ( s, shlex_object=False, com='', whi='' ):
    r"""
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

    >>> lex( "Yozza # a comment you dont want to see", whi=' ', com='#' )
    ['Yozza']

    """

    tokens = shlex( StringIO( s )) 
    tokens.commenters = com         
    tokens.whitespace = whi         

    if shlex_object:
        return tokens
    else:
        return list( tokens )

class CommandOutput( object ):

    # TODO: docstrings, and ellipsis


    def __init__(self, out=None, err=None, returncode=None, cmd=None ):
        self.out, self.err, self.returncode = out, err, returncode
        self.cmd = cmd

    def __str__(self):
        return self.out or "<Empty CommandOutput>"
    
    __repr__ = __str__
        
    def __neq__(self, other ):
        return not self.__eq__(other)

    def __eq__(self, other ):

        if isinstance(other, basestring):
            return other==self.out

        attrs = 'out', 'err', 'returncode'
        if not all( [ hasattr( other, a ) for a in attrs ]):
            raise TypeError("equality: argument must either a string or a CommandOutput instance.")
        
        return all( [ 
                getattr( self, a ) == getattr( other, a ) 
                for a in attrs 
                if getattr( other, a ) is not None 
                and getattr( self, a ) is not None ] )

    def exited_gracefully(self):
        return self.returncode==0

    def aborted(self):
        return self.returncode!=0


class CommandRunner ( object ):
    r"""
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

    # TODO: get the return value and the stderr

    stderr_on_stdout = True

    def __enter__( self ):
        self.stderr_dir = STDOUT if CommandRunner.stderr_on_stdout else PIPE

        self.shell = Popen( "sh", shell=True, stdin=PIPE, stdout=PIPE, stderr=self.stderr_dir )
        self.stdout_tokens = ShellSessionParser(self.shell.stdout)
        return self

    def __call__( self, cmd):
        r"""in it and sends it to the shell via stdin. Then, stdout is
        read until a prompt following a linefeed. The prompt is
        suppressed and the tokens read are joined and returned as
        the"""

        # TODO: set the returncode, get stderr if needed, use the CommandOutput: 
        # TODO: set the ellipsis

        self.shell.stdin.write(cmd + '\necho "~$ "\n')
        return self.stdout_tokens.get_output()
        
    def __exit__( self, *arg):
        self.shell.terminate()
        # If the child shell is hanged, maybe self.p.send_signal( signal.SIGKILL )
        # is more robust

class OutputReporter( object):

    def failed( self, inc=1 ):
        self.counters[0]+=inc

    def passed( self, inc=1 ):
        self.counters[1]+=1

    def __init__(self ):
        self.list = []
        self.counters = 0, 0 

    def append( self, output, expected):

        if not all( [ hasattr( output, a ) for a in ('out', 'err', 'returncode') ]):
            raise TypeError("argument must have the 'out', 'err', 'returncode' attributes.")

        self.failed() if output.aborted() else self.passed()

        self.list.append((output, expected))
        return output

    def report(self, verbose=False):

        return '\n'.join( 
            [   "Trying:\n\t%s\nExpecting:\n\t%s\n" % ( output.cmd, expected )
                + "Failed, got:\n\t%s\n" % output if output!=expected else "ok"
                for output, expected in self.list ] 
            + [ self.summary() ]) 
    
    __call__=report

    def summary( self ):
        return '\n'.join( [ 
                "%s test found\n%s test passed and %s test failed" % ( self.passed(0) + self.failed(0) ), 
                "Test passed." if self.failed(0)==0 else "***Test failed*** %s failures" % self.failed(0)
                ] )

def test( f ):

    report = OutputReporter()
    with CommandRunner() as run:
        for cmd, expected in ShellSessionParser( f ):
            if report.append( run( cmd ), expected ).aborted():
                print( "Something broke, I am bailing out, you get to keep both pieces.")
                break
    return report

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
    
    # for f in files: print test( f ).report( verbose=False )
        
    text=( "~$ ls\n"
           "coucou\n"
           "~$ tr\n"
           "passwd:" )
    print [ ( c,o) for c,o in ShellSessionParser(s=text) ]
                
