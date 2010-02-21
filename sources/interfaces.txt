
.. _interfaces:

Interfaces
==========

.. to build the documentation, the zope.schema package must be
.. installed

Overview
--------

.. automodule:: interfaces

*Wordish* makes use of five python modules from the standard library:

- :mod:`shlex` parses text, 

- :mod:`itertools` provides :func:`takewhile` functions and others
  functional tools,

- :mod:`StringIO` adapts a character string to the interface of an
  open file.

- :mod:`re` is the regular expression module, 

- :mod:`sys`, among others, gives access to the command line
  arguments, and the exit status.

Also, the required additional module, :mod:`docutils` offers the tools
to filter text in the *restructured text* format.


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

.. .. autoclass:: interfaces.NodeMatch
..    :members:
..    :undoc-members:

.. autoclass:: interfaces.BlockFilter
   :members:
   :undoc-members:






