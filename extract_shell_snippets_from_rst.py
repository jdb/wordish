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
        if self.content[0].split()[0]=='sh':
            return [ nodes.literal_block( 
                    text='\n'.join(self.content[2:]), 
                    language='sh' ) ]

rst.directives.register_directive( "sourcecode", SourceCode )


for i in core.publish_doctree(file(sys.argv[1]).read()).traverse():
    if i.tagname=='literal_block' and i.attributes.has_key('language'):
        print i.astext()


