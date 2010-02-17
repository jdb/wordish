
.. _interfaces:

Interfaces
==========

.. to build the documentation, the zope.schema package must be
.. installed

Overview
--------

.. automodule:: interfaces

Wordish makes use of five python modules from the standard library:

- :mod:`shlex` offers to tokenize text, 

- :mod:`itertools` offers the :func:`takewhile` functions and others
  functional tools,

- :mod:`StringIO` adapts a character string to the interface open
  file.

- :mod:`re` is the regular expression module, 

- :mod:`docutils` offers the tools to filter text in the
  *restructured text* format.

- :mod:`sys`, among others, gives access to the command line
  arguments.


Interfaces
----------

.. autoclass:: interfaces.ShellSessionParser
   :members:
   :undoc-members:

.. autoclass:: interfaces.CommandRunner
   :members:
   :undoc-members:

.. autoclass:: interfaces.CommandOutput
   :members:
   :undoc-members:

.. autoclass:: interfaces.Reporter
   :members:
   :undoc-members:

.. autoclass:: interfaces.NodeMatch
   :members:
   :undoc-members:

.. autoclass:: interfaces.BlockFilter
   :members:
   :undoc-members:






