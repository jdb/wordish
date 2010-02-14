"""


    filter = BlockSelector( directive='sourcecode', arg=['sh'] )
    with Shell() as run:
        for cmd, expected in ShellSessionParser( filter(f) ):
            if run( cmd ) != expected:
                print "unexpected command %s 's output"


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

# I would rather have the output command manipulated explicitly the
# branching into failed or success also done explicitly.

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
