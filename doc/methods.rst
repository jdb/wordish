
.. _methods:

Organisation
============

Some issues are tedious to deal with ona regular basis, for examples:

- synchronizing the version in multiples files,

- ensuring that all tests pass when releasing,

- publishing the software module and documentation where the users
  expects them,

If handled correctly, the developer can focus on the features, it is
more fun, and the users gets awesome softwares.

Ressources
----------

The sources are kept in a git repository on github
(http://github.com/jdb/wordish/), because git is a powerful source
configuration management that the author wishes to learn. Install the
``git`` commands on your system (sometimes packaged as ``git-core``)
and use the following to retrieve the sources::

    git clone git://github.com/jdb/wordish.git

The released software module is available on the `Python package index`_
and can be installed using *easy_install* or *pip*

.. _`Python package index`: http://pypi.python.org/pypi/wordish.


Github also provides a handy way to publish the documentation on the
web. The documentation sources are located in the *doc/* source
directory and are composed of restructured text pages built by the
Sphinx documentation system. The output of Sphinx are nice static html
pages which can be copied to the *gh-pages* special branch of the git
repository. Github treats the branch specially by serving this branch_
through the web at this url: http://jdb.github.com/wordish/.

.. _branch: http://github.com/jdb/wordish/tree/gh-pages 

There is an issue tracker at http://github.com/jdb/wordish/issues.


There is also a wiki_ automatically set up by github, but the author
has a personal preference for using a good text editor on files than
typing characters in a web form.

.. _wiki: http://wiki.github.com/jdb/wordish/ 

Version
-------

Whenever the code changes, the version gets incremented. The version
number is based on the concpet of ``public interfaces`` and backward
compatibility. For this project, the version number is composed of
three numbers: *major.minor.patch*

#. if the changes are seamless for the user, then the patch gets
   incremented. Usually, internal refactoring or backward compatible
   bugfixes cause a bump in the patch number,

#. if the user has access to new features, if the changes are
   substantial and backward compatible, the minor number gets
   incremented.

#. the major number is incremented when the user will have to change
   the way it uses the software. The major number is bumped when
   backward incompatible changes are introduced.

Ok, there is a fourth number: the pre-release number suffixed to the
version after the *b* letter (for *beta*), example: *1.2.3b7*. The
pre-release number is here to indicate that the software will soon be
released as *1.2.3*.
  
To retrieve the specific sources which were used to build a release,
for example version 1.0.0b7 use the tag::

  git clone git://github.com/jdb/wordish.git v1.0.0b7

Release
=======

Three steps :

#. As the user may request a version change, or because the version
   must be incremented between two uploads, prior to build the new
   version must be pushed wherever the version is mentionned :

   - in the documentation (in *doc/conf.py*), 

   - in the Python packaging configuration (in the *setup.py*) [#]_,

   - and in the *Wordish* python module itself, ( in the module constant
     ``__version__``).

   - The version file will also be used when building the *man page* as
     well as when building debian and fedora packages.

   This step is skipped if no upload and no version change was
   requested.

   The version is kept in a file named ``version`` and is pushed
   explicitly in the files with sed. The setup.py file should not read
   and depend on the version file at execution time, because at
   install time the version file is not available anymore.

   The inclusion of the version in the software module make it
   possible for users of the module to adapt their use to multiple
   wordish version depending on the software module version.

   Before commiting, the setup.py's *long_description* parameter and
   the README.txt are also updated with the latest docstring from the
   *wordish* module.

   .. the process is missing a release note howto built from the git
   .. log and formatted into the debian or rpm changelog, the tar ball
   .. does not the man pages nor the documentation

   .. this whole process is super tightly linked to git, github,
   .. python distutils

#. The tests are tried, the documentation is rebuilt, the package is
   rebuilt. Any error bailout the release script. This step is
   idempotent except for the documentation in the gh-branch which gets
   commited (not pushed).

   The scripts stops here if upload was not specified as an argument.

#. If an upload was requested, if the repository is not clean or if
   the current branch is not master, the script bails out.

In the *wordish* sources, the version is kept in the file named
version. The version is inserted :



The long description in the Python packaging configuration (in the
*setup.py*), is also updated from the *wordish* module docstring.

.. - *tests* give some trust that the code is stable. Trust means you
..   worry less, and you have more brain power for creative stuff. 

..   It ease refactoring, and testing for regression because they execute
..   in batch. It also define the scope of the behavior.


Documentation
=============

There are four sources for documentation: 

#. the wordish module docstrings which is copied into README.txt, the
   *long description* of the setup.py,

#. the *doc/* directory which is transformed into html pages stored in
   the branch gh-pages. This is a special convention of github which
   interpret these file to be presented on the project page.

#. the sources for the man pages in the *man/* directory are
   restructured text pages built into the *man format* 

#. the wordish public API is described in the *interfaces.py* file


Deployment
==========

Wordish is available on the Python package index, writing only a file 

.. - there are two audiences for deployment must be adapted:

..   - Python developers do not want the overhead of multiple
..     architecture, or requireing root access, Python packaging is just
..     what they need. 

..   - users and administrators have trust in their distributions only,
..     and do not want to learn one deployment system per programming
..     langage. There is potentially much more users than Python
..     developers.


.. _testsuitequestions:

.. Questions
.. ~~~~~~~~~

        .. refactor the tests
        ..     some are harmful for readability
        ..     some are not useful
        ..     some pertinent tests are missing
        ..     some should doctest instead of unittest and vice versa
        ..     distinction should be made between testing the public api and the rest
        ..     have I used backdoors?
        ..     are interface tested?
        ..     am i white box or black box
        ..     how to put the simple session and the git howto in the test_wordish

.. _buildchain:

.. From sources to packaging and deployment (no page yet)
.. ------------------------------------------------------

        .. source, branches and versions
        .. packaging
	.. documentation

.. _testbuildchain:

.. Questions
.. ~~~~~~~~~

.. _doc:

.. Wordish's documentation on its documentation (no page yet)
.. ----------------------------------------------------------



