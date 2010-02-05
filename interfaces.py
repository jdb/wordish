

from zope.interface import Interface
from zope.schema import Int, Text

# todo, doctest the public API

class ISessionParser( Interface ):
    """
    Created with an opened file argument containing a session, the
    constructor should accept a list of *prompts* for the second
    argument.

    For the session parser, a session begins with a prompt, then the
    command follows until the end of the command which is usually a
    newline, except when the newline is nested in curl brackets or
    parentheses, then follows the output which ends with a newline and
    a prompt.
    
    This object is meant to be called as part of a for loop or a
    generator expression, the next() method returns iteratively a list
    of two elements: a command and an output. 

    For each command and output, it is expected that the command will
    be executed by a *ICommandRunner* and the output given for a
    *IReporter* object in charge of comparing the output to the actual
    result of the application.
    """

    def next():
        """" 
        Returns a tuple whose first element is a command, and
        second element is an output.
        """

    def script( header=True ):
        """
        Writes the script and the cleanup script, named after the
        name of the article.
        """

class INodeMatch( Interface ):

    directive = Text()
    arguments = List( Text() )
    options   = Dict( Text():Text() )
    
    def __call__( doctreeelement ):
        """
        Given a doctree element, for example given as part of a
        doctree.traverse(), returns True if matches the constraints.
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
        Setup the ressource which is meant to be sent commands.
        """

    def __exit__():
        """
        Release the ressource.
        """

    def __call__( cmd ):
        """
        Send the command to the ressource, parses the output to return
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
    expected = ICommandOutput()

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
