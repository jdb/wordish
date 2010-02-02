#!/usr/bin/python

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass
import sys
from pprint import pprint
from docutils import core, nodes
from docutils.parsers import rst


class SourceCode( rst.Directive ):

    has_content = True

    def run( self ):
        self.assert_has_content()
        
        return [ nodes.literal_block( text='\n'.join(self.content[2:] )) ]

rst.directives.register_directive( "sourcecode", SourceCode )

for i in core.publish_doctree(file(sys.argv[1]).read()).traverse():
    if i.tagname=='literal_block':
        print i.astext()


