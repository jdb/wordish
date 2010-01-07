

from unittest import TestCase, main
from wordish import shell
from wordish import ShellSessionParser
from wordish import CommandOutput

class ShellTestCase( TestCase ):

    def setUp():
        "before"

        # should create a file and test the file is here
        # should test a return code of zero 
        # should test a return code different from zero
        # should test echoing to stdin as well as stdout

    def tearDown():
        "after"

class OutputComparisonTestCase( TestCase ):

    def setUp():
        "before"

    def tearDown():
        "after"

    

class ShellSessionParserTestCase( TestCase ):

    def setUp( self ):
        "before"
        self.tokens = [1,2,3] 
        
    def commenttest():
        """comments"

        comments should be stripped without consuming the
        linefeed. Commenters are set to the empty string and the
        comment tokenization is re=implemented"""

        raise NotImplemented

    def prompttest( self ):
        """prompt in comments"

        comments can contains a prompt"""

        raise NotImplemented


    def functiontest( self ):
        "parse a function"

        raise NotImplemented

    def sub_process( self ):
        "subprocess"

        raise NotImplemented

    def echotest( self ):
        """echo foobar

        the command and output should be separated"""
        
        raise NotImplemented

    def output_token_test(self):
        pass
        

    def tearDown( self ):
        "after"


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
