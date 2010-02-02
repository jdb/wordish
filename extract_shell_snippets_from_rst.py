#!/usr/bin/python

"""

"""


from docutils.nodes import literal_block, Text
from docutils.parsers import rst

class SourceCode( rst.Directive ):

    has_content = True
    def run(self):
        
        self.assert_has_content()
        return [ literal_block( text='\n'.join(self.content[2:] ))]

from docutils.parsers.rst import directives
directives.register_directive( "sourcecode", SourceCode )

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass
import sys
from docutils.core import publish_doctree

from lxml.etree import parse

for i in publish_doctree( file( sys.argv[1] ).read() ):
    if i.tagname=='literal_block':
        print i.astext()

