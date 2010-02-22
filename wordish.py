"""
Wordish is a script which executes a shell session parsed from a
documentation in the restructured text [#]_ format, then tests and builds a
report of the execution. To mark up shell code in an article,
*wordish* uses the custom directive ``sourcecode``, with the rquired
argument ``sh``. When presented with an article:

#. *wordish* filters out the text which is not marked with
   ``sourcecode``,

#. then, separates the blocks of shell codes between *commands* and
   *outputs*: 

   #. *wordish* consumes the prompt, parses for the newline which ends
      command,

   #. then parses for the prompt which ends the output, 

Example::

  .. sourcecode:: sh

     ~$ echo "hello world"   # Mmmh, insightful comment
     hello world

This simply renders like:

.. sourcecode:: sh

   ~$ echo "hello world"   # Mmmh, insightful comment
   hello world

The *command* starts after the prompt ("~$ ") and continues until the
first newline is found in the source code block. Here, it is just
after the word ``comment``. The command is ``echo "hello world" # Mmmh,
insightful comment`` The output is the text block found until the next
prompt: this is ``hello world``. There are **two** possible prompts:
``~$``, and ``~#``. Both are required to be followed by a space are are
treated the same.

Note: the newlines which are nested in curly brackets or parentheses are
**not** interpreted as an *end of command* character. Shells do the same:
curly brackets are used to define functions and parentheses makes the
nested command to be interpreted in a subprocess shell. The two
following examples from the introduction make it clear:

.. sourcecode:: sh

   ~$ (
   echo $((1+1)) )
   2

   ~$ sum () {
   echo $(( $1 + $2 ))
   }

The first command is ``echo $((1+1))`` in a subproces, and it's output
is ``2``. The second command is the definition of a function named
``sum`` and has no output. Defining functions sometimes clarify the
intent in subsequent uses of the function. For functions to be re-used,
the state of the shell must be kept between each snippets. *wordish*
keep a connection with the same *shell* subprocess (*bash* is used)
for the duration of the article.

.. sourcecode:: sh

   ~$ sum 42 58
   3

See how the output is obviously incorrect? we will see later how this
is reported.

When the output can not be completely predicted, such as when
displaying ``$RANDOM``, or displaying the size of a partitions in
bytes, there is a handy wildcard pattern which can be used:
``...``. It matches everything like ``.*`` in regexp [#]_.

.. sourcecode:: sh

   ~$ echo "a random number: " $RANDOM
   ...

One last thing, if a command does not exit gracefully, *wordish*
precautiously aborts, refusing to execute commands on the system under
test which is in an undefined state. *wordish* displays the remaining
unexecuted commands.

.. sourcecode:: sh

   ~$ What have the Romans ever done for us
   aqueduct? roads? wine !

   ~$ echo "Bye bye"
   Bye bye

This introduction is embedded in the wordish module as the
docstring. Just run *wordish* with no argument to get the example
report of this article:

.. sourcecode:: sh

   ~$ python -m wordish
   Trying:	echo "hello world"   # Mmmh, insightful comment...
   Expecting:	hello world
   ok
   
   Trying:	(
   echo $((1+1)) )
   Expecting:	2
   ok
   
   Trying:	sum () {
   echo $(( $1 + $2 ))
   }
   Expecting:	
   ok
   
   Trying:	sum 42 58
   Expecting:	3
   Failed, got:	100, 0
   
   Trying:	echo "a random number: " $RANDOM
   Expecting:	...
   ok
   
   Trying:	What have the Romans ever done for us
   Expecting:	aqueduct? roads? wine !
   Failed, got:	/bin/bash: line 19: What: command not found, 127
   
   Command aborted, bailing out
   Untested command:
   	echo "Bye bye"
        python -m wordish
   6 tests found. 
   4 tests passed, 2 tests failed.

There is another example real world article_ which is also included in
the sources distribution, and tested before each release. This is the
article which prompted the need for the development of *wordish*.

.. _article: http://jdb.github.com/sources/lvm.txt

.. [#] This syntax can be seen as light and readable version of html
       or latex, and was designed with the experience of existing Wiki
       syntaxes. The Sphinx project has a nice introduction_ on *rst*,
       the reference documentation is here_.

       .. _introduction: http://sphinx.pocoo.org/rest.html

       .. _here: http://docutils.sourceforge.net/rst.html#user-documentation

.. [#] Regexp are not directly used so that the various special regexp
       characters do not need to be escaped.

"""

__version__ = '1.0.2'

from subprocess import Popen, STDOUT, PIPE
from shlex import shlex 
from itertools import takewhile, chain
from StringIO import StringIO
import re
from docutils import core
from docutils.parsers import rst


def trace( decorated ):
    def f( *arg,**kwarg):
        print "%s: %s, %s => " % (decorated.__name__, arg, kwarg),
        ret = decorated( *arg,**kwarg )
        print ret
        return ret
    return f


class ShellSessionParser( object ):
    r"""
    An iterator which parses a text file of a shell session and yields
    pairs of commands and outputs
    
    >>> sess = ShellSessionParser( "~$ (echo coucou) # hello\ncoucou" )
    >>> for c,o in sess: print "command : %s\noutput  : %s" % (c,o)
    ...
    command : (echo coucou) # hello
    output  : coucou
    """

    def __init__( self, f, prompts=['~# ', '~$ '], com='', whi='' ):

        r"""
        The constructor takes a filename or an open file or a string
        as the shell session.

        The constructor sets the :attr:`tokens` member attribute with
        a shlex token stream initialised with the correct options for
        parsing comments and whitespace.
        
        The token commenters and whitespace are set to the empty string
        and can be modified with the function arguments 'com' and
        'whi'. 

        If the argument shlex_object is set to True then it'is not the
        list of tokens but the shlex object itself so that you can
        experiment with the :obj:`shlex` and it multiple attribute and
        method.

        >>> list(ShellSessionParser( "Yozza 1 2" ).tokens)
        ['Yozza', ' ', '1', ' ', '2']
        
        >>> tokens = ShellSessionParser( "Yozza 1 2").tokens
        >>> tokens.whitespace = ' '
        >>> list(tokens)
        ['Yozza', '1', '2']

        >>> list( ShellSessionParser("Yozza # a comment you dont want to see", whi=' ', com='#' ).tokens)
        ['Yozza']
        
        """
        
        self.tokens = shlex( f if hasattr(f, "read") else StringIO( f )) 
        self.tokens.commenters = com 
        # deactivate shlex comments facility which won't work for us.
        # The terminating linefeed means two things: end of comment an
        # end of command. As shlex consume the terminating linefeed,
        # there is no end of command left.
    
        self.tokens.whitespace = whi
        # deactivate shlex whitespace munging. characters cited in
        # ``shlex.whitespace`` are not returned by get_token. If
        # empty, whitespaces are returned as they are which is what we
        # want: they definitely count in bash, and may count in
        # output, so we just want to keep them as they are.

        self.nested = 0

        self.prompts = []
        for p in prompts:
            s=shlex(p)
            s.commenters, s.whitespace = com, whi
            self.prompts.append( list( s ) )

        self.max_prompt_len = max([ len(p) for p in self.prompts ])


    def _has_token( self ):
        r"""
        Returns False if the token list is empty (which usually means
        the end of file has been reached). Returns True otherwise.

        >>> sess = ShellSessionParser( "~$ env | grep USER\nUSER=jd" )
        >>> sess._has_token()
        True
        >>> for t in sess.tokens: pass
        >>> sess._has_token()
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
        if token == '\n' and self.nested==0:
            return False

        elif token in '({': self.nested += 1
        elif token in '})': self.nested -= 1

        return True

    def _takewhile( self, is_output=False ):
        r"""
        Returns a command or an output depending of the terminator
        provided. i.e. every token on which the terminator returns
        False. The terminator is a function which takes a token and
        returns whether the stream of tokens is terminated or not.

        >>> session = ShellSessionParser
        >>> session( "cmd" )._takewhile()
        'cmd'
        >>> session( "t () {\ncmd\n}\nhello" )._takewhile()
        't () {\ncmd\n}'
        """
        return ''.join (
            list( takewhile(
                    self.is_output if is_output else self.is_command, 
                    self.tokens )
                 ) ).strip()

    def _get_command(self):
        """
        Returns a string from the current token to the end of the
        next *command*.

        Maybe be confused about what is the end of a command when called
        in the middle of an output.
        """

        return self._takewhile(is_output=False)

    def _get_output(self):
        """
        Returns a string from the current token to the end of the
        next *output*.
        """

        return self._takewhile(is_output=True)

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
        self._get_output()
        while self._has_token() :
            yield self._get_command(), self._get_output()


    
    def toscript(self):
        commentize = lambda o: '# %s\n' % o.replace( '\n', '\n# ' )
        return "#!/bin/sh\nset -e  # -x\n\n%s\n" % '\n'.join(  
            chain( *( ( c, commentize(o) ) for c, o in self ) ) )


            
class CommandOutput( object ):

    # TODO: docstrings

    def __init__(self, out=None, err=None, returncode=None, cmd=None, match='ellipsis' ):
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
            return self.match( other, self.out )

        attrs = 'out', 'err', 'returncode'
        if any( [ not hasattr( other, a ) for a in attrs ]):
            raise TypeError( "equality: argument must either a "
                             "string or a CommandOutput instance.")
        
        return all( [ 
                self.match( str( getattr( other, a )) , str( getattr( self, a )))
                for a in attrs 
                if getattr( other, a ) is not None 
                and getattr( self, a ) is not None ] )

    def ellipsis_match(self,pattern,string):

        if '...' in pattern:
            start, end = pattern.split('...')
            return string.startswith(start) and string.endswith(end)
        else:
            return pattern==string

    def string_match(self,pattern,string):
        return pattern==string

    def re_match(self,pattern,string):
        return re.match(pattern, string) is not None

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
            self.shell = Popen( "/bin/bash", shell=True, 
                                stdin=PIPE, stdout=PIPE,stderr=PIPE, 
                                universal_newlines=True)
                                
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
        
        out =      self.stdout._takewhile( is_output=True )
        ret = int( self.stdout.tokens.next() )
        err =      self.stderr._takewhile( True 
                       ) if CommandRunner.separate_stderr else None 

        return out,err, ret

    def __exit__( self, *arg):
        self.shell.terminate()
        self.shell.wait()
        
        # If the child shell is hanged, maybe 
        # self.p.send_signal( signal.SIGKILL ) will be needed

class TestReporter( object):

    # should clearly present aborted from failed, and also not tested
    # will need a crazy dot graph to sort this mess
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

    def after(self, output ):
        self.last_output = output
        return self.passed( output 
                   ) if output==self.last_expected else self.failed( output )
    
    def summary( self ):
        print "%s tests found. " % (self.passcount + self.failcount)
        if self.failcount==0:
            print "All tests passed"
        else:
            print "%s tests passed, %s tests failed." % (
                self.passcount, self.failcount)

        return self.failcount
                

class BlockSelector( object):
    # this object could be a function after all, the prototype would
    # be a little more complex.

    # to build more complex node matching, cleanup, articles, it may
    # be easier to work on the doctree directly. Or the cleanup and
    # articles separators could be inlined in comments. Need to
    # clearify the ins and outs of both solutions. A shared instance
    # of this object is not thread safe. A function would be thread
    # safe but the class Directive would be redefined whenever called
    # which might not be a problem in our case, but is unneeded in the
    # general case.

    def __init__( self, directive='sourcecode', arg=['sh'] ):
        self.f = StringIO()

        class Directive( rst.Directive ):
            has_content = True
            def run( this ):
                this.assert_has_content()
                if this.content[0].split()==arg:
                    self.f.write( '\n'.join(this.content[2:])+'\n' )

                # The content could also be returned but it is not the
                # point, the point of this function is the side effect
                # of writing into self.f, which is done by now.
                return []

        rst.directives.register_directive( directive, Directive )

    def __call__( self, f ):
        # The following line is only good for its side effect of
        # filling self.f with the filtered content, that is why there
        # is no storage of the doctree.
        self.f.seek(0)
        self.f.truncate()
        core.publish_doctree(f.read()).traverse()
        self.f.seek(0)
        return self.f


#########
######### Console script entry points

import sys

def wordish():

    files = sys.argv[1:] if len( sys.argv ) > 1 else (StringIO( __doc__ ),)
    files = [ f if f!="-" else sys.stdin for f in files ] 
    files = [ f if hasattr(f, 'read') else file(f) for f in files ]

    ret = 0

    for f in files:

        report = TestReporter()
        filter = BlockSelector( directive='sourcecode', arg=['sh'])
        session = iter( ShellSessionParser( filter( f ) ))

        with CommandRunner() as run:
            for cmd, expected in session:

                print report.before( cmd, expected )
                print report.after( run( cmd ) )

                if report.last_output.aborted(): 

                    # sole condition if expected.returncode is None if
                    # expected returncode is not None and expected!=actual
                    # output should bailout. Test and errors should be
                    # different.

                    print( "Command aborted, bailing out")
                    remaining_cmds = [ cmd for cmd, _ in session ]
                    if len( remaining_cmds )==0:
                        print( "No remaining command" )
                    else:
                        print "Untested command%s:\n\t" % (
                            "s" if len( remaining_cmds )>1 else ""  ),
                        print( "\n\t".join( remaining_cmds ))

        ret += report.summary()
    return ret

def rst2sh():
    
    files = sys.argv[1:] if len( sys.argv ) > 1 else StringIO( __doc__ ),
    filter = BlockSelector( directive='sourcecode', arg=['sh'])
    for f in files: 
        print ShellSessionParser( 
            filter ( f  if hasattr(f, 'read') else file(f) )
            ).toscript()

if __name__=='__main__':
    sys.exit( wordish() )
    
                    
