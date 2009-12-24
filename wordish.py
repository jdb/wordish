#!/usr/bin/env python

from subprocess import Popen, PIPE
from shlex import shlex 
from itertools import takewhile


def get_pair( tokens ):

    tokens.wordchars += '{}()$.-'
    tokens.whitespace = ''
    tokens.commenters = ''

    [ t for t in get_output_token( tokens ) ]

    for t in tokens:

        if t==tokens.eof:
            raise StopIteration

        else:
            tokens.push_token(t)
            yield map(lambda l:''.join(l).strip(), [
                    ( t for t in get_command_token ( tokens ) ),
                    ( t for t in get_output_token  ( tokens ) )
                    ] )

def get_command_token( tokens, paren_nest=0,bracket_nest=0 ):

    for t in tokens:

        if t == '\n' and paren_nest==0 and bracket_nest==0:
            raise StopIteration

        if t == '#':
            [ t for t in takewhile(lambda t:t!='\n', tokens )]
            tokens.push_token('\n')
            raise StopIteration

        else:
            if   '(' in t: paren_nest   += 1
            elif ')' in t: paren_nest   -= 1
            elif '{' in t: bracket_nest += 1
            elif '}' in t: bracket_nest -= 1

            yield t

def get_output_token( tokens ):

    for t in tokens:
        if t!='~':
            yield t
        else:
            u=tokens.next()
            if u in '$#':
                raise StopIteration
            yield t+u

class Call ( object ):
    def __init__(self, cmd):
        p=Popen(cmd,shell=True, stdout=PIPE, stderr=PIPE)
        self.out, self.err = map(lambda s:s.strip(), p.communicate())
        self.returncode = p.returncode 

def preambule(command, expected_output):
    return  

def format_error(command, expected_output, output):

    return  "\n%s\nFailed example:\n\t%s\nExpected:\n\t%s\nGot:\n\t%s\n%s" % (
        '*' * 68, command, expected_output, output, '*' * 68)

if __name__=="__main__":

    import sys

    files = sys.argv[1:] if len(sys.argv)>1 else (sys.stdin,)
    for f in files:
        tokens = shlex( f if hasattr(f, "read") else file(f) )

        # Here I wold launch a bash session in a pty: with bash_session as b
        for c,o in get_pair (tokens):
            
            print( "Trying:\n\t%s\nExpecting:\n\t%s" % ( c, o ) )
            ans = Call( c )
            # here ans = b.call
            print( "%s" % ( "ok" if o==ans.out else format_error(c,o,ans.out) ) )
            if ans.err != '':
                print("%s\nWarning :\n\t%s\nWrote on stderr:\n\t%s\n%s" % (
                        '-' * 68, c, ans.err, '-' * 68 ))

            if ans.returncode !=0:
                print( "Something broke, I am bailing out, you get to keep the pieces. Sorry...")
                break



        # 1. shlex.wordchars : should have many more chars actually but which !
        # 2. test diagnostic should take err and returncode
        # 3. configurable prompt
        # 4. build a report
        # 5. --test should do black box testing
        # 6. functional tests are good 
        # 7. option -v should switch on the report, no -v should just report errors
        # 8. fixes comments and tests them

        # 8. must work with the lvm article
        # 9. must be hooked to the  sourcecode directive
        # done 10. must be called with python -m shdoctest done
        # 11. all commands should be sent to a bash in a single session as a **pty** 
        # 12. implement the ellipsis
