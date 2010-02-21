
.. _write:

How to write an article
=======================

.. automodule:: wordish


Debugging an article
====================

When debugging an article, repeatedly executing half of the commands,
I have found it handy to:

- write a cleanup script which resets the system under test to the
  initial state,

- use the ``false`` shell command in the articles, to explicitly
  require the execution to bail out at a certain point in the article,

- Use a log file with ``python -m wordish my_article.rst | tee
  my_article.log``


Installation
============

*Wordish* is available on the Python package index and can be
installed [#]_ with::

  sudo pip wordish

If you want to separate Python module from outside the debian or rpm
repositories, from the Python modules installed managed by your
distribution, you can use virtualenv_::

   virtualenv wordish_env && cd wordish_env
   source ./bin/activate
   pip wordish
   
At this point the wordish module is available in the Python path. You can
test it with::

   python -m wordish

This executes *wordish* on its docstrings, which is written in
restructured text.

.. [#] pip_ and distribute_ are the new black: *pip* takes care of
       fetching packages and dependencies while *distribute* takes
       care of the definition and the building of the package. They
       aims replace and be backward compatible with ``easy_install``
       and ``setuptools``.
 
       .. _pip: 

       .. _distribute:

.. _virtualenv:

