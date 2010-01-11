

from unittest import TestCase, main
from wordish import ShellSessionParser as session
from wordish import CommandRunner as shell
from wordish import OutputChecker as check
from wordish import CommandOutput as out
from collections import namedtuple


# TODO: command runner not tested: create file check existence, check
# enter, check exit

class CommandOutputTestCase ( TestCase ):

    def correct_attributes_test( self ):
        output = out()
        for attr in ["out","err","returncode"]:
            self.assertTrue(hasattr(out,attr))

    def equal_test( self ):
        outs, errs, rets = ["out",None], ["err",None], [1,None]
        cases = [ (out(o,e,r),out(o1,e1,r1)) for o in outs for e in errs for r in rets for o1 in outs for e1 in errs for r1 in rets]

        for parsed, actual in cases:
            self.assertTrue(parsed==actual)

    def equal_false_test( self ):
        outs, errs, rets = ["out",None], ["err",None], [1,None]
        outs1, errs1, rets1 =["hello",None], ["warn",None], [0,None]

        cases = [ (o,e,r,o1,e1,r1) for o in outs for e in errs for r in rets for o1 in outs1 for e1 in errs1 for r1 in rets1]
        cases = [ (out(o,e,r),out(o1,e1,r1)) for (o,e,r,o1,e1,r1) in cases if (o,e,r,o1,e1,r1) != (None, None, None, None, None, None)]

        for parsed, actual in cases:
            self.assertFalse(parsed==actual)

    def check_test( self ):
        _ = namedtuple("_", "attr")

        self.assertTrue( check( _(1), _(1),    "attr") is True  )
        self.assertTrue( check( _(1), _(2),    "attr") is False )
        self.assertTrue( check( _(1), _(None), "attr") is None  )

    def exit_gracefully_test( self ):
        self.assertTrue( out( returncode=0 ).exited_gracefully() )

class ShellSessionParserTestCase( TestCase ):

    def command_test (self):

        commands = (
            ("date\nls\nid\n", "date" ),
            ("date # comment\n", "date" ),
            ("ls # ~$ promptlike\n", "ls" )
            ( "hello () \n{ echo hello\n} \n some more stuff",
              "hello () \n{ echo hello\n}" ),
            ( "( cd \ntmp )\n", "( cd \ntmp )\n"),
            ( "ls", "ls"),
            ( "", "")
            )

        get_command=lambda text:session(s=text).take_until()
        for text, parsed in commands:
            self.assertEqual( self.get_command( text ), parsed)

    def output_test (self):

        outputs = (
            ("hello world\n~$ ", "hello world" ),
            ("hello world\n~good by\n~$ ", "hello world\n~good by" ),
            ( "~$ ", ""),
            ( "~# ", ""),
            ( "", ""),
            )

        get_output=lambda text:session(s=text, is_output=True ).take_until()
        for text, parsed in outputs:
            self.assertEqual( self.get_output( text ), parsed)



class shellTestCase():
    """
    """

    def create_shell_test(self):
        "the shell is created"
        
        raise NotImplemented

    def long_running_shell_test(self):
        "the shell is created"
        
        raise NotImplemented

    def destroy_test(self):
        "the shell is correctly destroyed"
        
        raise NotImplemented


class CheckerTestCase( object ):
    
    def setUp():
        "before"

    def launchtest():
        "execute a command"

        raise NotImplemented

    def errortest():
        "expect an error"

        raise NotImplemented

    def tearDown():
        "after"


if __name__ == '__main__':
   main()
