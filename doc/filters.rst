
.. _rst:

The restructured text and Sphinx format
=======================================

A central class of Wordish is the ShellSessionParser which takes a
string representing a shell session and yields pairs of (command,
output). The ShellSessionParser relies on filters to adapt the
articles file formats to extract the shell session. Wordish is able to
operate on three file formats:

1. a simple session log (for the extraction is already done),

2. a restructured text file (which requires the docutils package),

3. the sources of a Sphinx project


