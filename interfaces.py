"""
The *Wordish* modules declares three central classes: 

- the :class:`BlockFilter` which, given a directive, filters
  restructured blocks of text marked with the *directive* attribute of
  the object,

- the :class:`ShellSessionParser` which splits a shell session log into
  commands and outputs,

- and the :class:`CommandRunner` which spawns a shell subprocess, and
  to which the parsed commands are sent for execution,

The :func:`wordish` module function, which is the main entry point of
the script, requires a file descriptor *f* argument containing a shell
session in a restructured text article. A simplified version of
:func:`wordish` boils down to::

  filter = BlockFilter( directive='sourcecode', arg=['sh'] )
  with CommandRunner() as run:
      for cmd, expected in ShellSessionParser( filter( f ) ):
          if run( cmd ) != expected:
              print "Warning: unexpected command %s 's output"

*Wordish* also declares two additional classes:

- The :class:`Reporter` formats the parsed commands and output,
  accumulates the success and failures, and formats a report in the
  end.

- The :class:`CommandOutput` is used to model the ouput of a shell
  command: the message printed on stdout, the message printed on
  stderr, and the return code. The :meth:`CommandRunner.__call__`
  method returns instances of this class.

  A *CommandOutput* can be compared to a simple string, with the
  ``==`` or ``!=`` syntax (as in the example above), in which case,
  only the stdout message is used for the comparison.

The :func:`wordish` module function articulates the five classes::

    report = TestReporter()
    filter = BlockFilter(directive='sourcecode', arg=['sh'])

    with CommandRunner() as run:
        for cmd, expected in ShellSessionParser( filter(f) ):
            print report.before(cmd, expected)

            out = run(cmd)

            print report.success(out) if out == expected else report.failure(out)

            if out.aborted(): 
                print("there was a serious error: bailing out")
                break
"""


class ShellSessionParser( object ):
    """Created with an open file *f*, containing a shell text
    *session*, and optionally, *prompts*, the list of potential
    prompts in the session.

    A *session* begins with a prompt, then a *command* follows
    until a newline, except when the newline is nested in curly
    brackets or parentheses. Then follows the output which ends with a
    newline and a prompt.
    
    This object is an iterable, and can be called in a for loop or a
    generator expression: the next() method yields lists of two
    strings: a command and an output.

    The parsed commands can be sent to a *ICommandRunner* and the
    parsed output can be compared to the CommandOutput instance
    returned by the *ICommandRunner* 

    Also, The SessionParser is instantiated twice in the command
    runner, connected to the stdout and stderr files of the shell
    subprocess."""

    def next(self):
        """Returns a tuple whose first element is a command, and second
        element is an output."""

    def takewhile(self, is_output):
        """Returns a string composed of the tokens until a specific
        token: either an un-nested linefeed if the argument *is_output*
        is false, or a prompt if *is_output* is true."""

class CommandRunner( object ):
    """The CommandRunner is a context manager which runs a shell created
    only for the duration of a *with* python code block. A context
    manager is an object which can be called from a with statement.
 
    **The instance is a callable**, which takes, as first argument, a
    shell command to be executed, the stdin, stdout and returncode of
    the command is returned as an *OutputCommand*.

    On **entering the context**, setup the ressource (the shell) executing
    the commands. On **exiting the context**, terminate the shell.
    """

class CommandOutput( object ):
    """Structures the output of a standard shell command with the two
    strings read on stdout and stderr plus the returncode.

    The **equality operator** can be used with the CommandOutput, The
    equality operator expects either a string or a CommandOuput as a
    right hand side. The right hand side can contain the three dots
    pattern '...' to match anything.

    When matching against another CommandOutput, only the non null
    attributes are matched: output == CommandOutput(out=None,
    err=None, returncode=None) is always True."""
    
    out = None
    "The standard output channel"

    err = None
    "The standard error channel"

    returncode = None
    "The return code"

    
class Reporter( object ):
    """The Reporter methods are introduced between the calls to the
    SessionParser and the CommandRunner"""
    
    def before(self, cmd ):
        """Annonce the action to come. For example, the test to be
        done, the expected result. In case, the test takes time, it is
        desirable to let the user know what is happening beforehand."""

    def passed(self, output ):
        """Formats a successful result. Increment the *passed* counter"""

    def failed(self, output ):
        """Formats a failed result. Decrement the *passed* counter"""

    def summary(self):
        """Report the operations with, the number of actions, the
        number of success, the number of failure, etc."""
        

class NodeMatch( object ):
    """Given a doctree element, for example an element of
    doctree.traverse(), returns True if matches the constraints."""

    # Error, there is no more directive at this time
    node = None
    "Only node of this type will match"

    attributes   = None
    "A dictionary of attributes:values"
    

class BlockFilter( object ):
    """Given an open file on a restructured text document, returns an
    open file containing the text blocks marked up by the directive
    attribute."""

    directive = None
    "Only text marked up with this directive will be kept"

    arguments = None
    "A list of arguments"

    options   = None
    "A dictionary of options:values"
    
            
