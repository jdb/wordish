
.. _interfaces:

Interfaces and objects description
==================================

.. Overview
.. --------

.. parser
.. ------

.. output
.. ------

.. runner
.. ------

.. reporter
.. --------

Wordish makes use of five python modules from the standard library:
:mod:`shlex` offers to tokenize text, :mod:`itertools` offers
:func:`takewhile` functions and others functional tools,
:mod:`StringIO` adapts a character string to the interface open
file. :mod:`re` is the regular expression module, and :mod:`docutils`
offers the tools to filter text in the *restructured text*
format. :mod:`sys`, among others, gives access to the command line
arguments.


.. include:: ../interfaces.py
   :literal:
