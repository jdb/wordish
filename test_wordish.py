

import unittest, doctest, wordish
 
from wordish import ShellSessionParser as session
from wordish import CommandOutput as out
from wordish import CommandRunner as shell
from wordish import OutputReporter 



# TODO: command runner not tested: create file check existence, check
# enter, check exit

class CommandOutputTestCase(unittest.TestCase):

    def test_correct_attributes( self ):
        [ self.assertTrue(hasattr( out(), attr)) 
          for attr in ["out","err","returncode"] ]


    def test_equal( self ):
        true = self.assertTrue
        true( out( "hello world"), "hello world" )
        true( out( "hello world", "warning"), "hello world" )
        true( out( "hello world", "warning", -1 ), "hello world" )

        true( out( "hello world"), out("hello world") )
        true( out( "hello world", "warning"), 
              out( "hello world", "warning" ) )
        true( out( "hello world", "warning", -1 ), 
              out( "hello world", "warning", -1 ) )

        true( out(), out() )
        true( out(1, None, 1), out(None, 1, None) )
        true( out(1, None, None), out(None, 1, 1) )
        true( out(1 ), out(None, 1, 1) )

    def test_all_equal( self ):
        outs, errs, rets = ["out",None], ["err",None], [1,None]
        cases = [ (out(o,e,r), out(o1,e1,r1)) 
                  for o  in outs for e  in errs for r  in rets 
                  for o1 in outs for e1 in errs for r1 in rets ]

        [ self.assertTrue(parsed==actual) for parsed, actual in cases ]

    def test_equal_false( self ):
        outs1, errs1, rets1 =["hello",None], ["warn",None], [0,None]

        cases = [ (o1,e1,r1) for o1 in outs1 for e1 in errs1 for r1 in rets1]
        cases = [ (out('out','err',1), out(o1,e1,r1)) for (o1,e1,r1) in cases if (o1,e1,r1) != (None, None, None)]

        [ self.assertFalse(parsed==actual) for parsed, actual in cases ]
            
    def test_exit_gracefully( self ):
        self.assertTrue( out( returncode=0 ).exited_gracefully() )

class ShellSessionParserTestCase( unittest.TestCase ):

    def test_command (self):

        commands = (
            ("date\nls\nid\n", "date" ),
            ("date # comment\n", "date" ),
            ("ls # ~$ promptlike\n", "ls" ),
            ( "hello () {\n echo hello\n} \n some more stuff",
              "hello () {\n echo hello\n}" ),
            ( "( cd \ntmp )\n", "( cd \ntmp )"),
            ( "ls", "ls"),
            ( "", "") )

        for text, expected in commands:
            self.assertEqual( session(text).takewhile(), expected ) 


    def test_output (self):

        outputs = (
            ("hello world\n~$ ", "hello world" ),
            ("hello world\n~good by\n~$ ", "hello world\n~good by" ),
            ( "~$ ", ""),
            ( "~# ", ""),
            ( "", "") )

        for text, expected in outputs:
            self.assertEqual( session(text).takewhile(is_output=True), expected)

    def test_next ( self ):
        
        text=( "~$ ls\n"
               "coucou\n"
               "~$ tr\n"
               "passwd:" )

        self.assertEqual(
            list(session(text)),
            [ ("ls", "coucou"), ("tr", "passwd:") ]
            )

    def test_toscript ( self ):
        
        text= ( "~# ls\n"
               "coucou\nbonjour\n"
               "~# tr\n"
               "passwd:" )

        self.assertEqual(
            session(text).toscript(),
            ( "#!/bin/sh\nset -e\n#set -x\n"
              "ls\n"
              "# coucou\n"
              "# bonjour\n"
              "tr\n"
              "# passwd:\n" )
            )


    def test_executablescript ( self ):
        """make sure the script is executable """

        text=( "~# date >/dev/null \n"
               "coucou\nbonjour\n"
               "~# ls >/dev/null \n"
               "passwd:" )
        import os
        self.assertEqual( os.system(session(text).toscript()), 0)


class CommandRunnerTestCase( unittest.TestCase ):


    def test_simple_command( self ):
        "sh writes on stdout"

        with shell() as sh:
            out = sh('echo coucou')
        self.assertEqual( out.out, 'coucou' )

    def test_stderr( self ):
        "sh writes on stderr"
        with shell() as sh:
            out = sh('echo coucou >&2')
        self.assertEqual( out.err, 'coucou' )

    def test_returncode( self ):
        "return codes"

        with shell() as sh:
            out = sh('true')
        self.assertEqual( out.returncode, 0 )

        with shell() as sh:
            out = sh('false')
        self.assertEqual( out.returncode, 1 )

    def test_sequence_of_command( self ):

        with shell() as sh:
            zero =  sh('export coucou=1').returncode
            zero += sh('test $coucou==1').returncode
            zero += sh('myfunc () { echo coucou ; return 42 ; }').returncode
            zero += sh('myfunc').returncode
            zero += sh('( echo $coucou )').returncode
        
        self.assertEqual( zero, 42 )

    def test_enter( self ):
        """use enter(), ask for the shell pid, check with the os that
        the process with this pid is 'sh'"""
        
        with shell() as sh:
            self.assertTrue( sh.shell.pid > 0)
        
    def test_exit(self):
        """Check that the pid of the shell does not exist anymore, or
        is not the son of this python object"""
        
        with shell() as sh:
            pass
        self.assertEqual(sh.shell.returncode, -15)


class ReporterTestCase( unittest.TestCase ):

    def test_counters_and_append(self):
        report = OutputReporter()
        for i in range(10):
            report.before("", out(returncode=0))
            report.result( out(returncode=i))

        self.assertEqual(report.failcount,9)
        self.assertEqual(report.passcount,1)

if __name__ == '__main__':
   
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ShellSessionParserTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CommandOutputTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CommandRunnerTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ReporterTestCase))

    suite.addTest(doctest.DocTestSuite(wordish))

    unittest.TextTestRunner(verbosity=2).run(suite)
   
