
.. _methods:

Development methods
===================

In a software project, it is often the case that the issues
surrounding coding are more difficult and less fun than the
development itself. Issues like managing the sources, testing,
documenting, releasing properly and tracking tickets takes some focus,
if they are handled properly, then you regain brain power for
interesting stuff, you are able to pile new features beacuase
fondations are more stable, you do not worry about them anymore.

We want

- an easy way to find the right *sources*, 

  - clean sources, 

  - latest sources commited for backup or synchronisation with other
    people,
  
  - sources corresponding to a released version,

- *version* should tell whether new versions :
  
  - just fix typos and bugs,

  - or bring new features in a backward compatible way, 

  - or present backward incompatible change,

- *tests* give some trust that the code is stable. Trust means you
  worry less, and you have more brain power for creative stuff. 

  It ease refactoring, and testing for regression because they execute
  in batch. It also define the scope of the behavior.

- the *documentation* shold be included in the source, contains
  information for different audiences,
 
  - the scope of the application, the feature list, the help required
    for *user* to feel at ease with the software features,

  - developpers may wish to see the design, the interfaces
    documentation

- there are two audiences for deployment must be adapted:

  - Python developers do not want the overhead of multiple
    architecture, or requireing root access, Python packaging is just
    what they need. 

  - users and administrators have trust in their distributions only,
    and do not want to learn one deployment system per programming
    langage. There is potentially much more users than Python
    developers.
!
This section explains how this modest project is set up, so that
contributions and futurs development are easy.

.. _scm:

Source management
-----------------

The code is hosted on github: three branches, are used:

- *next* contains the day to day commits, it is sometimes broken, 

- *master* contains a clean state of the sources, a contributor will
  likely use this branch,

- *gh-pages* is a convention at github.com: it is meant to contain
  static html files. The branch *gh-pages* of the repository
  github.com/jdb/wordish is automatically served at the address
  http://jdb.github.com/wordish



.. _testsuite:

Test suites
-----------

Two kinds of test:

- unit tests: the file ``test_wordish``

-



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



