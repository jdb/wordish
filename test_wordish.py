
import unittest, doctest, wordish
from StringIO import StringIO 
from wordish import ShellSessionParser as session
from wordish import CommandOutput as out
from wordish import CommandRunner
from wordish import TestReporter 
from wordish import BlockFilter
from tempfile import mkstemp
from subprocess import Popen
import sys, os

# TODO: command runner not tested: create file check existence, check
# enter, check exit

class CommandOutputTestCase(unittest.TestCase):

    def ellipsis(self, *args):
        return out(*args, match='ellipsis')
    
    def re(self, *args):
        return out(*args, match='re')

    def setUp(self):

        self.true_examples = ( 
            (( "hello world", None, None),   ( "hello world", None, None )),
            (( "hello world", "warn", None ),( "hello world", None, None )),
            (( "hello world", "warn", -1 ),  ( "hello world", None, None )),
            (( "hello world", "warn"),       ( "hello world", "warn", None )),
            (( "hello world", "warn", -1 ),  ( "hello world", "warn", -1 )),
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
            for want, got in samples:
                self.assertTrue( out(*want)==out(*got) )

        for want, got in self.false_combinatorial:
            self.assertFalse( out(*want)==out(*got) )
            
    def test_equal_re( self ):

        for samples in (self.true_examples, self.true_combinatorial,
                        self.true_re):
            for want, got in samples:
                self.assertTrue( self.re(*want)==self.re(*got) )

        for samples in self.false_combinatorial, self.false_re:
            for want, got in samples:
                self.assertFalse( self.re(*want)==self.re(*got) )

    def test_equal_ellipsis( self ):
          
        for samples in (self.true_examples, self.true_combinatorial,
                        self.true_ellipsis):
            for want, got in samples:
                self.assertEqual( self.ellipsis(*want),self.ellipsis(*got) )

        for samples in self.false_combinatorial, self.false_ellipsis:
            for want, got in samples:
                self.assertFalse( self.ellipsis(*want)==self.ellipsis(*got) )

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

        for text, want in commands:
            self.assertEqual( session(text).takewhile(), want ) 


    def test_output (self):

        outputs = (
            ("hello world\n~$ ", "hello world" ),
            ("hello world\n~good by\n~$ ", "hello world\n~good by" ),
            ( "~$ ", ""),
            ( "~# ", ""),
            ( "", "") )

        for text, want in outputs:
            self.assertEqual( session(text).takewhile(is_output=True), want)

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

        with CommandRunner() as sh:
            out = sh('echo coucou')
        self.assertEqual( out.out, 'coucou' )

    def test_stderr( self ):
        "sh writes on stderr"
        with CommandRunner() as sh:
            out = sh('echo coucou >&2')
        self.assertEqual( out.err, 'coucou' )

    def test_bashism( self ):
        "handy bash curly brackets"
        with CommandRunner() as sh:
            out = sh('echo a{b,c}')
        self.assertEqual( out.out, 'ab ac' )

    def test_returncode( self ):
        "return codes"

        with CommandRunner() as sh:
            out = sh('true')
        self.assertEqual( out.returncode, 0 )

        with CommandRunner() as sh:
            out = sh('false')
        self.assertEqual( out.returncode, 1 )

    def test_sequence_of_command( self ):

        with CommandRunner() as sh:
            zero =  sh('export coucou=1').returncode
            zero += sh('test $coucou==1').returncode
            zero += sh('myfunc () { echo coucou ; return 42 ; }').returncode
            zero += sh('myfunc').returncode
            zero += sh('( echo $coucou )').returncode
        
        self.assertEqual( zero, 42 )

    def test_enter( self ):
        """use enter(), ask for the shell pid, check with the os that
        the process with this pid is 'sh'"""
        
        with CommandRunner() as sh:
            self.assertTrue( sh.shell.pid > 0)
        
    def test_exit(self):
        """Check that the pid of the shell does not exist anymore, or
        is not the son of this python object"""
        
        with CommandRunner() as sh:
            pass
        self.assertEqual(sh.shell.returncode, -15)


class ReporterTestCase( unittest.TestCase ):

    def test_counters_and_append(self):
        report = TestReporter()
        exp = out(returncode=0)
        for i in range(10):
            report.before("a cool command", 'cmd')
            report.passed() if exp==out(returncode=i) else report.failed() 


        self.assertEqual(report.failcount,9)
        self.assertEqual(report.passcount,1)

class BlockFilterTestCase( unittest.TestCase ):

    def test( self ):

        article=StringIO("""
This article is going to get me to the Pulitzer prize.

.. codesource:: blabi

   ~$ echo coucou
   coucou

supercalifragilisticexpialidocious

""")

        want = "~$ echo coucou\ncoucou\n"

        filter = BlockFilter(directive='codesource', arg=['blabi'])
        self.assertEqual(filter(article).read(), want)


class HintsTestCase( unittest.TestCase ):

    # classes which requires a conf cannot be tested without a conf
    # the conf is expected global while this test case can not declare 
    # a global conf object. The wordish objects can all take an optional conf
    # attribute which override the global configuration. 

    def execute(self, s):
        with CommandRunner() as run:
            return all([run(cmd)==want for cmd,want in session(s)])

    def test_ignore(self):
        s="""
~$ echo hello
hello
~$ echo coucou   # ignore
something different from coucou
~$ echo coucou
coucou
"""
        self.assertTrue(self.execute(s)) 

    def test_returncode(self):

        s="""
~$ echo hello
hello
~$ false   # returncode=1
~$ echo coucou
coucou
"""
        self.assertTrue(self.execute(s)) 

    def test_stderr(self):
        s="""
~$ echo hello
hello
~$ ls $RANDOM   # on stderr
ls: cannot access ...: No such file or directory
~$ echo coucou
coucou
"""
        self.assertTrue(self.execute(s)) 
            
if __name__ == '__main__':
   
    suite = unittest.TestSuite()

    add = lambda t: [ suite.addTest(unittest.TestLoader(
            ).loadTestsFromTestCase(i)) for i in t ]

    add( [ CommandOutputTestCase, 
           HintsTestCase, 
           ShellSessionParserTestCase,
           CommandRunnerTestCase, 
           ReporterTestCase, 
           BlockFilterTestCase ] )

    suite.addTest(doctest.DocTestSuite(wordish))

    run = unittest.TextTestRunner(verbosity=1).run(suite)

    if len(run.errors)!=0 or len(run.failures)!=0:
        sys.exit(1)
