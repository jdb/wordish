
import unittest, doctest, wordish
from StringIO import StringIO 
from wordish import ShellSessionParser as session
from wordish import CommandOutput as out
from wordish import CommandRunner as shell
from wordish import TestReporter 
from wordish import BlockSelector
import sys

# TODO: command runner not tested: create file check existence, check
# enter, check exit

class CommandOutputTestCase(unittest.TestCase):

    def ellipsis(self, *args):
        return out(*args, match='ellipsis')
    
    def re(self, *args):
        return out(*args, match='re')

    def setUp(self):

        self.true_examples = ( 
            (( "hello world", None, None),                ( "hello world", None, None)),
            (( "hello world", "warning", None ),     ( "hello world", None, None )),
            (( "hello world", "warning", -1 ), ( "hello world", None, None )),     
            (( "hello world", "warning"),      ( "hello world", "warning", None )),
            (( "hello world", "warning", -1 ), ( "hello world", "warning", -1 )),
            (( None, None, None),              ( None, None, None)),
            (( 1, None, 1),                    (None, 1, None) ),
            (( 1, None, None),                 (None, 1, 1)),
            (( 1, None, None ),                            (None, 1, 1)))
        
        outs, errs, rets = [ "hello", None ], [ "watchout", None ], [ 0, None ]

        self.true_combinatorial = ( 
            ((o,e,r), (o1,e1,r1)) 
            for o  in outs for e  in errs for r  in rets 
            for o1 in outs for e1 in errs for r1 in rets )

        self.false_combinatorial = (
            (('bye','fail',1), (o,e,r)) for o in outs for e in errs for r in rets 
            if (o,e,r) != (None, None, None) )

        self.true_ellipsis = ( 
            (( "random 1832345 lucky me !",), ( "random ... lucky me !",)   ),
            (( "random foobar lucky me !",),  ( "random ... lucky me !",)   ),
            (( "random '' lucky me !",),      ( "random '...' lucky me !",) ))

        self.false_ellipsis = (
            (( "random 832345 lucky me",), ("random  ... lucky me",)),  
            (( "random 18345\nlucky me",), ("random ... lucky me" ,)),  
            (( "random 1324",),            ("random ... lucky me" ,)),  
            (( "1832345 lucky me",),       ("random ... lucky me" ,)))  

        self.true_re = ( 
            (( "random 1832345 lucky me !",), ("random .*? lucky me !"   ,)),
            (( "random foobar lucky me !",),  ("random .*? lucky me !"   ,)),
            (( "random '' lucky me !",),      ("random '.*?' lucky me !" ,)))

        self.false_re = (
            (( "random 832345 lucky me",),  ("random  .*? lucky me" ,)), 
            (( "random 18345\nlucky me",),  ("random .*? lucky me"  ,)), 
            (( "random 1324",),             ("random .*? lucky me"  ,)), 
            (( "1832345 lucky me",),        ("random .*? lucky me"  ,))) 


    def test_correct_attributes( self ):
        for attr in ["out","err","returncode"]:
            self.assertTrue( hasattr( out(), attr) ) 

    def test_equal_string( self ):

        for samples in self.true_examples, self.true_combinatorial: 
            for parsed, actual in samples:
                self.assertTrue( out(*parsed)==out(*actual) )

        for parsed, actual in self.false_combinatorial:
            self.assertFalse( out(*parsed)==out(*actual) )
            
    def test_equal_re( self ):

        for samples in (self.true_examples, self.true_combinatorial,
                        self.true_re):
            for parsed, actual in samples:
                self.assertTrue( self.re(*parsed)==self.re(*actual) )

        for samples in self.false_combinatorial, self.false_re:
            for parsed, actual in samples:
                self.assertFalse( self.re(*parsed)==self.re(*actual) )

    def test_equal_ellipsis( self ):
          
        for samples in (self.true_examples, self.true_combinatorial,
                        self.true_ellipsis):
            for parsed, actual in samples:
                self.assertTrue( self.ellipsis(*parsed)==self.ellipsis(*actual) )

        for samples in self.false_combinatorial, self.false_ellipsis:
            for parsed, actual in samples:
                self.assertFalse( self.ellipsis(*parsed)==self.ellipsis(*actual) )

    def test_exit_gracefully( self ):
        self.assertTrue( out( returncode=0 ).exited_gracefully() )

class ShellSessionParserTestCase( unittest.TestCase ):

    def test_command (self):

        commands = (
            ("date\nls\nid\n", "date" ),
            ("date # comment\n", "date # comment" ),
            ("ls # ~$ promptlike\n", "ls # ~$ promptlike" ),
            ( "hello () {\n echo hello\n} \n some more stuff",
              "hello () {\n echo hello\n}" ),
            ( "( cd \ntmp )\n", "( cd \ntmp )"),
            ( "ls", "ls"),
            ( "", "") )

        for text, expected in commands:
            self.assertEqual( session(text)._takewhile(), expected ) 


    def test_output (self):

        outputs = (
            ("hello world\n~$ ", "hello world" ),
            ("hello world\n~good by\n~$ ", "hello world\n~good by" ),
            ( "~$ ", ""),
            ( "~# ", ""),
            ( "", "") )

        for text, expected in outputs:
            self.assertEqual( session(text)._takewhile(is_output=True), expected)

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
            ( "#!/bin/sh\nset -e  # -x\n\n"
              "ls\n"
              "# coucou\n"
              "# bonjour\n\n"
              "tr\n"
              "# passwd:\n\n" )
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

    def test_bashism( self ):
        "handy bash curly brackets"
        with shell() as sh:
            out = sh('echo a{b,c}')
        self.assertEqual( out.out, 'ab ac' )


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
        report = TestReporter()
        for i in range(10):
            report.before("", out(returncode=0))
            report.after( out(returncode=i))

        self.assertEqual(report.failcount,9)
        self.assertEqual(report.passcount,1)

class BlockSelectorTestCase( unittest.TestCase ):

    def test( self ):

        article=StringIO("""
This article is going to get me to the Pulitzer prize.

.. codesource:: blabi

   ~$ echo coucou
   coucou

supercalifragilisticexpialidocious

""")

        expected = "~$ echo coucou\ncoucou\n"

        filter = BlockSelector(directive='codesource', arg=['blabi'])
        self.assertEqual( filter(article).read(), expected)
            

if __name__ == '__main__':
   
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ShellSessionParserTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CommandOutputTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CommandRunnerTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ReporterTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(BlockSelectorTestCase))
    suite.addTest(doctest.DocTestSuite(wordish))

    # ce qui aurait pu etre completement possible au lieu de parser
    # deux fois, c'est que la directive source code 

    run = unittest.TextTestRunner(verbosity=2).run(suite)

    if len(run.errors)!=0 or len(run.failures)!=0:
        sys.exit(1)
