#!/usr/bin/env python

from subprocess import Popen, STDOUT, PIPE
from shlex import shlex 
from itertools import takewhile
from StringIO import StringIO

def lex ( s, shlex_object=False, com='', whi='' ):
    """
    Returns the list of tokens of the input string.

    The token commenters and whitespace are set to the empty string
    and can be modified with the function arguments 'com' and
    'whi'. 

    If the argument shlex_object is set to True then it'is not the
    list of tokens but the shlex object itself so that you can
    experiment with the :obj:`shlex` and it multiple attribute and
    method.

    >>> lex( "Yozza 1,2" )
    ['Yozza', ' ', '1', ',', '2']

    >>> tokens = lex( "1 2", shlex_object=True )
    >>> tokens.whitespace = ' '
    >>> [t for t in tokens ]
    ['1', '2']

    >>>> lex( "Yozza # you dont want to see that", whi=' ', com='#' )
    ['Yozza']
    """

    tokens = shlex( StringIO( s )) 
    tokens.commenters = com         
    tokens.whitespace = whi         

    if shlex_object:
        return tokens
    else:
        return list( tokens )

class ShellSession( object ):
    """
    An iterator which parses a text file of a shell session and yields
    pairs of commands and outputs
    
    >>> session = ShellSession( StringIO( "~$ echo coucou\ncoucou" ))
    >>> for c,o in session: print c,o
    ...
    echo coucou coucou
    """

    def __init__( self, f=None, s=None ):
        """
        The constructor takes a filename or an open file or a string
        as the shell session.

        The constructor sets the :attr:`tokens` member attribute with
        a shlex token stream initialised with the correct options for
        parsing comments and whitespace.
        """

        self.tokens = shlex( f if hasattr(f, "read") else file( f ) )

        self.tokens.commenters = '' 
        # comments are broken for commands, le retour chariot qui signifie
        # la fin d'une commande est consomme par les commentaires, la
        # commande est incorrectement termine.
    
        self.tokens.whitespace = ''
        # characters cited in ``shlex.whitespace`` are not returned by
        # get_token. If empty, whitespaces are returned as is which is
        # what we want: they definitely count in bash, and may count in
        # output, so in just do not munge them.

    def has_token( self ):
        """
        Return True when there are token available, False if the
        stream token is empty.

        >>> session = ShellSession( s="~$ env | grep USER\nUSER=jd" ))
        >>> session.has_token()
        True
        >>> for c,o in session: pass
        >>> sesssion.has_token()
        False
        """
        t = self.tokens.get_token()
        return False if t==self.tokens.eof else self.tokens.push_token( t ) or True


    def get_command( self, nested=0 ):
        """
        Returns the command i.e. everything except comments, until a
        linefeed except when the linefeed is nested in parentheses and
        brackets.

        >>> session = ShellSession( s="true")
        >>> session.get_command()
        true
        >>> ShellSession( s="true\n" ).get_command()
        true
        >>> ShellSession( s="(true\n)" ).get_command()
        (true
        )
        >>> ShellSession( s="t () {\ntrue\n)" ).get_command()
        t () {
        true
        }
        """

        c = []

        for t in self.tokens:
            
            if t == '\n' or t == '#' or t==self.tokens.eof:
                
                if t=='#': 
                    
                    [ t for t in takewhile( lambda t:t!='\n', self.tokens )]
                    t = '\n'
	
                if nested==0:
                    return ''.join(c).strip()
	
            elif t in '({': nested += 1
            elif t in '})': nested -= 1
	
            c.append( t )

        return ''.join(c).strip()
	
    def get_output( self ):
        """
        Returns the output i.e. everything until the prompt ``~$``, or ``~#``
        terminated by a mandatory space.
        """
        
        o = []

        for t in self.tokens:
            
            if t=='~':
                n1, n2 = [ self.tokens.next(), self.tokens.next() ]
                if n1 in '$#' and n2 == ' ':
                    return ''.join( o ).strip()
                else:
                    self.tokens.push( n1 ) 
                    self.tokens.push( n2 )
                    
            o.append( t )

        return ''.join( o ).strip()

    def __iter__(self):
        return self

    def next(self):
        self.get_output()
        while self.has_token() :
            return self.get_command(), self.get_output() 
        raise StopIteration


class SubShell ( object ):
    """
    Implements a python "context manager", when entering the context,
    create a shell in a subprocess, the call method takes a string
    with a shell command and execute it in the shell. call ret output of the command.

    >>> with shell() as sh:
    ...    sh.call("echo coucou")
    ...    sh.call("a=$((1+1))")
    ...    sh.call("echo $a")
    ...
    coucou
    2

    Note: for this kind of interactive stuff, maybe a pty is more
    appropriate. ssh does that and bash behaves a bit differently when
    run hooked to a pty.    
    """

    # __init__
    # kill_on_exit=False
    # stderr_on_stdout=False


    def __enter__(self):
        self.shell = Popen( "sh", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT )
        self.stdout_tokens = ShellSessionParser(self.shell.stdout)
        return self

    def call(self, cmd):
        """in it and sends it to the shell via
    stdin. Then, stdout is read until a prompt following a
    linefeed. The prompt is suppressed and the tokens read are joined
    and returned as the"""

    # should return a namedtuple out, err and returncode whose equald
    # is configurable ellipsis=...  the matching object has out, err,
    # returncode and an equal method which takes in account, stderr,
    # stdout and returncode if set. It should be possible to check
    # that return code is fine without bothering with the output. This
    # equald should also match against a simple string.

        self.shell.stdin.write(cmd + '\necho "~$ "\n')
        return self.stdout_tokens.get_output()
        
    def __exit__(self, *arg):
        # could be more robust, and kill the subprocess on exit
        # instead of asking the shell to terminate.
        self.p.stdin.write("exit\n")
        self.p.communicate()


def format_error(command, expected_output, output):
    return  "\n%s\nFailed example:\n\t%s\nExpected:\n\t%s\nGot:\n\t%s\n%s" % (
        '*' * 68, command, expected_output, output, '*' * 68)


if __name__=="__main__":

    import sys

    if len(sys.argv)>1 :
        files = sys.argv[1:] 
    else:
        from StringIO import StringIO
        files = StringIO("""
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


#     for f in files:

#         session = ShellSessionParser( f )

#         with SubShell() as shell:

#             for c,o in session:

#                 print( "Trying:\n\t%s\nExpecting:\n\t%s" % ( c, o ) )

#                 ans = shell.call( c )

#                 print( "%s" % ( "ok" if o==ans else format_error( c, o, ans ) ) )

                # if ans.err != '':
                #     print("%s\nWarning :\n\t%s\nWrote on stderr:\n\t%s\n%s" % (
                #             '-' * 68, c, ans.err, '-' * 68 ))
                # 
                # if ans.returncode !=0:
                #     print( "Something broke, I am bailing out, you get to keep the pieces. Sorry...")
                #     break

        #  object ShellSessionParser object output matcher has an

        #  equal oprator return out,err and returncode which can be
        #  configured with matching only out by default but also the
        #  rest if needed, taking the ellipsis in account if needed.

        #  configurable command prompt in 
        #  build a report

        #  functional tests are good 
        #  option -v should switch on the report, no -v should just report errors
        #  fixes comments and tests them

        #  must work with jdb's lvm article
        #  must be hooked to the sourcecode directive standalone, sphix and docutils
        #  all commands should be sent to a bash in a single session as a **pty** 
        #  implement the ellipsis in checking the return of the 

        # python -m wordish --test should show something
        # python -m wordish simple_session.txt should show something
        # python -m unittest -v wordish test_wordish should show something
                
