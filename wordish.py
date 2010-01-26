"""
For an administrator or a developer, many operations are usually
carried out via a command line interface, or a *shell*. Such
operations include, for example, disk partitioning, raid setup or
volume snapshots. They can also include source version control
tutorial, or software packaging howto. Network and firewall setup,
remote administration or load balancing tunings are few other examples
naturally operated with a shell.

Wordish is a project which executes a shell session parsed from a
documentation then tests and builds a report of the execution. The
article contains the commands and the expected outputs, the report
takes care of comparing the expected results with the actual output of
the execution of the command to make sure the documentation is correct. 

Wordish can test wordy shell articles. 
"""

from subprocess import Popen, STDOUT, PIPE
from shlex import shlex 
from itertools import takewhile, chain
from StringIO import StringIO
import re


def trace( decorated ):
    def f( *arg,**kwarg):
        print "%s: %s, %s => " % (decorated.__name__, arg, kwarg),
        ret = decorated( *arg,**kwarg )
        print ret
        return ret
    return f


def lex ( f, shlex_object=False, com='', whi='' ):
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

    tokens = shlex( f if hasattr(f, "read") else StringIO( f )) 
    tokens.commenters = com 
    # deactivate shlex comments facility which won't work for us.
    # The terminating linefeed means two things: end of comment an
    # end of command. As shlex consume the terminating linefeed,
    # there is no end of command left.
    
    tokens.whitespace = whi
    # deactivate shlex whitespace munging. characters cited in
    # ``shlex.whitespace`` are not returned by get_token. If
    # empty, whitespaces are returned as they are which is what we
    # want: they definitely count in bash, and may count in
    # output, so we just want to keep them as they are.

    if shlex_object:
        return tokens
    else:
        return list( tokens )


class ShellSessionParser( object ):
    r"""
    An iterator which parses a text file of a shell session and yields
    pairs of commands and outputs
    
    >>> sess = ShellSessionParser( "~$ (echo coucou\n) # hello\ncoucou" )
    >>> for c,o in sess: print c,o
    ...
    (echo coucou
    ) coucou
    """

    # several hints could be parsed in the comments on a command:
    # ignore, stderr/&2, maybe ask input, they should be returned

    def __init__( self, f, prompts=['~# ', '~$ '] ):
        """
        The constructor takes a filename or an open file or a string
        as the shell session.

        The constructor sets the :attr:`tokens` member attribute with
        a shlex token stream initialised with the correct options for
        parsing comments and whitespace.
        """        
        self.tokens = lex( f, shlex_object=True)
        self.nested = 0

        self.prompts = [ lex(p) for p in prompts ]
        self.max_prompt_len = max([ len(p) for p in self.prompts ])

    def has_token( self ):
        r"""
        Return True when there are still tokens available, False if
        the stream token is empty.

        >>> sess = ShellSessionParser( "~$ env | grep USER\nUSER=jd" )
        >>> sess.has_token()
        True
        >>> for t in sess.tokens: pass
        >>> sess.has_token()
        False
        """
        t = self.tokens.get_token()
        return False if t==self.tokens.eof else self.tokens.push_token( t ) or True

    
    def is_output( self, token ):
        r"""
        Returns true if the token is after the last token of the
        output of a command, else returns false. The functions stops
        right before the prompt which can be either '~# ' or '~$ '.

        >>> sess = ShellSessionParser( "youpi\n~# " )
        >>> sess.tokens.next()
        'youpi'
        >>> sess.is_output( 'youpi' )
        True
        >>> sess.tokens.next(),sess.tokens.next()
        ('\n', '~')
        >>> sess.is_output( '~' )
        False
        """
        # TODO: in the unittest, make sure '~' occurs in the -1, -2, and -3 position.
        # also  make sure it occurs in the three last position at the same time.

        if token in [ p[0] for p in self.prompts ]:
            tokens = [token,] + [ self.tokens.next() 
                                  for i in range( self.max_prompt_len - 1) ] 

            return False if any([tokens==p for p in self.prompts ]) else (
               [ self.tokens.push_token(t) for t in reversed(tokens[1:]) ] or True)
        else:
            return True

    def is_command( self, token ):
        r"""
        Returns true if the token is after the last token of a command
        in the section, else returns false. The functions stops right
        before the linefeed but only when the linefeed is not nested in
        brackets or parenthesis.

        >>> sess = ShellSessionParser( "date\n" )
        >>> sess.tokens.next()
        'date'
        >>> sess.is_command( 'date' )
        True
        >>> sess.tokens.next()
        '\n'
        >>> sess.is_command( '\n' )
        False

        This is the end of output, since the linefeed was not nested.

        >>> sess = ShellSessionParser( "(youpi\n)\n" )
        >>> [ sess.is_command( sess.tokens.next()) for i in range(3) ]
        [True, True, True]
        >>> sess.is_command( sess.tokens.next()); sess.is_command( sess.tokens.next()); 
        True
        False
        
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
        False. The terminator is a function which takes a token and
        returns whether the stream of tokens is terminated or not.

        >>> session = ShellSessionParser
        >>> session( "cmd" ).takewhile()
        'cmd'
        >>> session( "t () {\ncmd\n}\nhello" ).takewhile()
        't () {\ncmd\n}'
        """
        return ''.join (
            list( takewhile(
                    self.is_output if is_output else self.is_command, 
                    self.tokens )
                 ) ).strip()

    get_command = lambda self:self.takewhile()
    get_output  = lambda self:self.takewhile(is_output=True)

    def __iter__(self):
        r"""
        Returns the next pair of command and output.

        TODO: some unittest on the corner cases: empty file, only command, only outputs

        >>> session = ShellSessionParser
        >>> sess = session( "~# cmd\noutput\n~# true\n" )
        >>> for c,o in sess: print "command: %s\noutput: %s" % (c,o)
        command: cmd
        output: output
        command: true
        output: 
        """
        self.takewhile( is_output=True ) 
        while self.has_token() :
            yield self.takewhile(), self.takewhile( is_output=True )
    
    def toscript(self):
        commentize = lambda o: '# %s\n' % o.replace( '\n', '\n# ' )
        return "#!/bin/sh\nset -e  # -x\n\n%s\n" % '\n'.join(  
            chain( *( ( c, commentize(o) ) for c, o in self ) ) )


            
class CommandOutput( object ):

    # TODO: docstrings

    def __init__(self, out=None, err=None, returncode=None, cmd=None, match='string' ):
        self.out, self.err, self.returncode = out, err, returncode
        self.cmd = cmd

        assert match in ['string', 're', 'ellipsis']
        self.match = getattr(self, match + '_match')

    def __str__(self):
        """
        The string representation of a CommandOutput is a comma
        separated list of the non null value of the out, err and
        returncode members (in this order).

        >>> CommandOutput(out=1,err=2,returncode=3)
        1, 2, 3

        >>> CommandOutput(out="2010-01-22")
        2010-01-22
        """
        return ', '.join( [ str( getattr(self,a) )
                            for a in 'out', 'err', 'returncode' 
                            if not(getattr(self,a) in [None, ''])
                            ] )
    
    __repr__ = __str__
        
    def __neq__(self, other ):
        return not self.__eq__(other)

    def __eq__(self, other ):

        if isinstance(other, basestring):
            return other==self.out

        attrs = 'out', 'err', 'returncode'
        if any( [ not hasattr( other, a ) for a in attrs ]):
            raise TypeError( "equality: argument must either a "
                             "string or a CommandOutput instance.")
        
        return all( [ 
                self.match( getattr( other, a ), getattr( self, a ) )
                for a in attrs 
                if getattr( other, a ) is not None 
                and getattr( self, a ) is not None ] )

    def ellipsis_match(self,pattern,string):
        # the pattern should be first escaped from special characters
        # except the three dots '...'  what are the special
        # characters?
        return re.match(pattern.replace('...','.*?'), string) is not None

    def string_match(self,pattern,string):
        return pattern==string

    def re_match(self,pattern,string):
        return re.match(pattern.replace('...','.*'), string) is not None

    def exited_gracefully(self):
        return self.returncode==0

    def aborted(self):
        return self.returncode!=0


class CommandRunner ( object ):
    r""" Implements a python "context manager", when entering the
    context (the *with* block ), creates a shell in a subprocess,
    right before exiting the context (leaving the block or processing
    an exception), the shell is assured to be terminated.

    The call method takes a string meant to contain a shell command
    and send it to the shell which executes it. call ret output of the
    command.

    >>> with CommandRunner() as sh:
    ...    sh("echo coucou")
    ...    sh("a=$((1+1))")
    ...    sh("echo $a")
    ...
    coucou, 0
    0
    2, 0
    """
    separate_stderr = True

    def __enter__( self ):
        if CommandRunner.separate_stderr:
            self.terminator = '\necho "~$ $?" \n' + 'echo "~$ " >&2 \n' 
            self.shell = Popen( "sh", shell=True, 
                                stdin=PIPE, stdout=PIPE,stderr=PIPE)
                                
            self.stdout = ShellSessionParser( self.shell.stdout )
            self.stderr = ShellSessionParser( self.shell.stderr ) 
        else:
            self.terminator = '\necho "~$ " \n' 
            self.shell = Popen( "sh", shell=True, 
                                stdin=PIPE, stdout=PIPE, stderr=STDOUT)

            self.stdout = ShellSessionParser( self.shell.stdout )
            self.stderr = None
        return self

    def __call__( self, cmd):
        r"""in it and sends it to the shell via stdin. Then, stdout is
        read until a prompt following a linefeed. The prompt is
        suppressed and the tokens read are joined and returned as
        the"""

        self.shell.stdin.write( cmd + self.terminator )
        return CommandOutput( *self.read_output(), cmd=cmd )
 
    def read_output(self):
        
        out =      self.stdout.takewhile( is_output=True )
        ret = int( self.stdout.tokens.next() )
        err =      self.stderr.takewhile( True ) if CommandRunner.separate_stderr else None 

        return out,err, ret

    def __exit__( self, *arg):
        self.shell.terminate()
        self.shell.wait()
        
        # If the child shell is hanged, maybe 
        # self.p.send_signal( signal.SIGKILL ) will be needed

class OutputReporter( object):

    def __init__( self ):
        self.passcount, self.failcount = 0, 0
        self.last_expected, self.last_output = None, None

    def failed( self, output ):
        self.failcount += 1
        return "Failed, got:\t%s\n" % output 

    def passed( self, output):
        self.passcount += 1
        return "ok\n"

    def before( self, cmd, expected ):
        self.last_expected = expected
        return "Trying:\t\t%s\nExpecting:\t%s" % ( cmd, expected )

    def result(self, output ):
        self.last_output = output
        return self.passed( output ) if output==self.last_expected else self.failed( output )
    
    def summary( self ):
        print "%s tests found. " % (self.passcount + self.failcount)
        if self.failcount==0:
            print "All tests passed"
        else:
            print "%s tests passed, %s tests failed." % (self.passcount, self.failcount)
                
            
def run( f ):

    report = OutputReporter()

    with CommandRunner() as run:
        for cmd, expected in ShellSessionParser( f ):

            print report.before( cmd, expected )
            print report.result( run( cmd ) )

            if report.last_output.aborted():
                print( "Something broke, I am bailing out, "
                       "you get to keep both pieces.")
                break
    report.summary()

simple_example = """
~$ echo "hello world"   # insightful comment
hello world

~$ (
echo $((1+1)) )
2

~$ sum () {
echo $(( $1 + $2 ))
}

~$ sum 42 58                # correct command, erroneous output
3

~$ What have the Romans ever done for us   #  command not found: will abort
...
aqueduct ?
roads
wine !
"""


#########
######### Console script entry points

import sys

def wordish():

    files = sys.argv[1:] if len( sys.argv ) > 1 else (StringIO( simple_example ),)
    for f in files: 
        run( f  if hasattr(f, 'read') else file(f) )
      
def rst2sh():
    
    files = sys.argv[1:] if len( sys.argv ) > 1 else StringIO( simple_example ),

    for f in files: 
        print ShellSessionParser( f  if hasattr(f, 'read') else file(f) ).toscript()

if __name__=='__main__':
    wordish()
                    

