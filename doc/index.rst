

Wordish documentation
=====================

*Wordish can test wordy shell documentation*. 

For an administrator or a developer, many operations are carried out
via a command line interface, also known as a *shell*. The list of
examples is endless and includes for example:

- source version control, software packaging or deployment, 

- disk partitioning, raid setup or volume snapshots, 

- network and firewall setup, remote administration or load balancing
  tunings. 

*Wordish* is a script which executes a shell session parsed from a
documentation in the restructured text format, then tests and builds a
report of the execution. The documentation should contain the commands
and the expected outputs, *Wordish* takes care of comparing the
expected results with the actual output of the execution of the
command to make sure the documentation is correct.


Reader's guide
--------------

- Administrators will find the few rules and installation procedure
  in the page :ref:`write`. The page :ref:`roadmap` shows the
  direction of the project.

- Anyone curious of how *Wordish* is designed may be interested in
  the :ref:`interfaces`,

- For the brave Python developper impatient to propose a feature
  patch, a bug report and a fix, the page describing the
  :ref:`methods` will hopefully help him get started.


..    The author of these lines must say that he found there are many
..    ways to do *testing* and *packaging* and he would be grateful for
..    any reader's advices on the existential questions listed :ref:`here
..    <testsuitequestions>` and :ref:`here <testbuildchain>`


Project ressources
------------------

Wordish uses github_ for source control, documentation_ and
bugs_. Deployment is done via the `Python package index`_.

.. _github: http://github.com/jdb/wordish/

.. _documentation: http://jdb.github.com/wordish/

.. _bugs: http://github.com/jdb/wordish/issues

.. _`Python package index`: http://pypi.python.org/pypi/wordish


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

