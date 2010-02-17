"""
The *Wordish* modules declares three central classes: 

- the :class:`BlockSelector` which, given a directive, filters restructured text, 

- the :class:`ShellSessionParser` which split a shell session log into
  commands and outputs,

- and the :class:`CommandRunner` which spawns a shell subprocess, and
  to which it sends the parsed the parsed commands for execution,

The :func:`wordish`, which is the main entry point of the script,
requires a file descriptor *f* argument describing a shell session in
a restructured text article. It boils down to::

  filter = BlockSelector( directive='sourcecode', arg=['sh'] )
  with CommandRunner() as run:
      for cmd, expected in ShellSessionParser( filter( f) ):
          if run( cmd ) != expected:
              print "Warning: unexpected command %s 's output"

*Wordish* also declares two additional classes:

- The :class:`Reporter` formats the parsed commands and output,
  accumulates the success and failures, and formats a report in the
  end.

- The :class:`CommandOutput` is used to model the ouput of a command
  which is composed of the message printed on stdout, the message
  printed on stderr, and the return code. The
  :meth:`CommandRunner.__call__` method output instances of this class.

  A *CommandOutput* can be compared to a simple string, as in the
  example above, in which case, only the stdout message is taken in
  account.

The five classes articulate, in the :func:`wordish` module: 

.. sourcecode:: python

    report = TestReporter()
    filter = BlockSelector( directive='sourcecode', arg=['sh'] )
    
    with CommandRunner() as run:
        for cmd, expected in ShellSessionParser( filter(f) ):
    
            print report.before( cmd, expected )
            output = run( cmd )
            
            if output == expected :
                print report.success( output )
            else
                print report.failure( output )
    
                if report.last_output.aborted(): 
                    print("there was a serious error: bailing out")
                    break
"""

from zope.interface import Interface, Attribute
from zope.schema import Int, Text

# todo, doctest the public API

class ISessionParser( Interface ):
    """
    The first argument should an opened file argument containing a
    *session*, the constructor should accept a list of *session
    prompts* strings for the second argument.

    A *session* begins with a prompt, then a *command* follows until a
    newline, except when the newline is nested in curly brackets or
    parentheses. Then follows the output which ends with a newline and
    a prompt.
    
    This object is an iterable, and can be called with a for loop or a
    generator expression: the next() method yields lists of two
    strings: a command and an output.

    The parsed commands can be sent to a *ICommandRunner* and the
    parsed output, to a *IReporter* in charge of comparing the output
    to the actual result of the application. Also, The ICommandRunner has
    two ISessionParser set to its shell  XXXXXXXXXX
    """

    def next():
        """
        Returns a tuple whose first element is a command, and second
        element is an output.
        """

    def script( header=True, name="filename" ):
        """
        Writes the script and the cleanup script, named after the name
        of the article.
        """

    def takewhile( is_output ):
        """
        Low level functions useful in a XXXXXXXXXXXXXX
        """

class ICommandRunner( Interface ):
    """
    The ICommandRunner is a context manager which runs a shell created
    only for the duration of a *with* python code block. 

    The class instance is callable and is given by the
    *ISessionParser* the shell command to be executed, the result of
    the command is structured and returned as an *OutputCommand*.
    """
    
    def __enter__():
        """
        Setup the ressource (the shell) executing the  commands.
        """

    def __exit__():
        """
        Terminate the shell.
        """

    def __call__( cmd ):
        """
        Send the command to the shell, parses the output to return
        an ICommandOutput instance.
        """

class ICommandOutput( Interface ):
    """
    This class structures the output of a standard shell command with
    the two strings stdout and stderr plus the returncode.
    """
    
    "the standard output channel"
    out = Text()

    "the standard error channel"
    err = Text()

    returncode = Int( min=0 )

    def __eq__( other ):
        """
        The current output object can be compared with another object
        for equality.

        Depending on the needs, only the standard output is taken in
        account, or for instance, the standard output is a second
        check provided the returncode is zero.
        """

    
class IReporter( Interface ):
    """
    The IReporter methods are introduced between the calls to the
    ISessionParser and the ICommandRunner
    """

    """The expected output is presented and set by before(). It is
    stored to be later compared to the actual output by after()"""
    expected = Attribute("an ICommandOutput()")

    def before( cmd, expected ):
        """
        Annonce the action to come. For example, the test to be done,
        the expected result. In case, the test takes time, it is
        desirable to let the user know what is happening beforehand.
        """

    def after( output ):
        """
        Process and present the result.
        """

    def summary():
        """
        Conclude the operations with, for instance, the number of
        actions, the number of success, the number of failure.
        """

class IDocutilsNodeMatch( Interface ):

    directive = Text()
    arguments = Attribute( "a list of arguments") 
    options   = Attribute( "a dictionary of options:values") 
    
    def __call__( doctreeelement ):
        """
        Given a doctree element, for example given as part of a
        doctree.traverse(), returns True if matches the constraints.
        """
