


from unittest import TestSuite

from shdoctest import Call

class CallTestSuite( object ):

    def setUp():
        "before"

        # should create a file and test the file is here
        # should test a return code of zero 
        # should test a return code different from zero
        # should test echoing to stdin as well as stdout

    def tearDown():
        "after"

class ParserTestSuite( object ):

    def setUp():
        "before"

    def echotest():
        "echo foobar"
        
        raise NotImplemented


    def functiontest():
        "parse a function"

        raise NotImplemented

    def sub_process():
        "subprocess"

        raise NotImplemented

    def tearDown():
        "after"

class CheckerTestSuite( object ):
    
    def setUp():
        "before"

    def launchtest():
        "execute a command"

        raise NotImplemented

    def errortest():
        "expect an error"

        raise NotImplemented

    def launchtest():
        "execute a command"

        raise NotImplemented

    def tearDown():
        "after"
