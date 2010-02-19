
.. _roadmap:

Limitations and roadmap
=======================


Integration with Sphinx
-----------------------

- Sphinx integration, how to to reuse ``sourcecode``, so the directive
  accepts the options ``ignored``, ``cleanup option``,
  ``no_check``, ``can_abort``,

- configuration: bailout_on_abort, match=string|re|ellipsis, prompts,
  ignore_stderr, 

- use the Sphinx logging system which can be shut from the command line,

- build a directive ``test_report`` inserting a table report in the
  doc,

- build a directive ``article`` which takes the name of the article,
  and for each, creates a command runner and accumulate the cleanup
  code, in case of an abort.

.. pr plan
..     shunit
..     jo lange
..     ubuntu server
..     sphinx
..     docutils
..     lvs
..     btrfs, lvm
..     debian administration
..     python/debian/ubuntu planet/mailing list
..     anevia
..     roming
..     imil


Python/debian packaging
-----------------------

- use *distribute* to benefit from ``console_script``, and dependency
  resolution (docutils), and also because it is the new black. Maybe
  *pip* knows how to install man pages and re-hash the man-db,

- how to package the future *sphinx.ext.wordish* (should the
  repository be on bitbucket),

- command line argument: ``--help``, ``--quiet``, ``--prompt``,
  ``--match 'exact|ellipsis|regexp'``, ``--cleanup mycleanup.sh``,
  ``ignore_stderr``, ``bailout_on_abort``

- how to use git branches to ease debian and rpm packaging? (do like
  the documentation on github with the gh-pages)

..
  la creation de la directive source prend le renvoie une queue sous
  la forme d'une stringio, la directive source code écrit dans cette
  stringio que le session parser consomme.

  Le doctree généré est jeté, on s'en sert juste pour lancer la
  directive sourcecode, tout en effet de bord. (on evite peut etre
  aussi la latence au démarrage)

  Ca ne sert pas a grand chose d'utiliser le session parser pour
  réinserer des noeuds command et output sous la forme de literal block
  dans la mesure ou il seront disjoint dans le doc final. Sauf si un
  réèl builder html/latex implémnte un IReporter

Interfaces
----------

- How to declare that a class implements a *context manager*, an
  *iterable*, that a member attribute is a list of certain class or a
  dictionary,

- Use epydoc, or Sphinx syntax to specify the signature of methods and
  objects,

Tests
-----

- some impede readability, some are redundant, some use backdoors,
  some important one tests may be missing, some doctest would better
  be unit test and vice versa,

- clear distinction between public (black box) and private api (white
  box). Proof test est the public API at least,

- some black box testing may be needed to be launched as root and be
  run on every file in *examples/*,


objects and interfaces
----------------------

- **ISessionParser**

  - *Universal* linefeed for commands in articles written on Windows, 

  - Like doctest, write hints for wordish to adjust its behavior when
    parsing hints in the comment after a command::

       ~$ echo boilerplate      # ignore
       wildly unpredictable

       ~$ echo coucou >&2       # &2
       coucou

       ~$ She is a witch        # returncode: 127
       She: command not found

       ~$ rm -r ./temp_mount_point   # cleanup

    The returned expected could be an CommandOutput instead of simple
    string and carry the attribute *ignore*, *returncode*, *cleanup*
    or *err*. 

    The idea for the *cleanup* command is to execute them on
    bailout, as they are meant to return the system in predictable
    state.

  .. - If *wordish* could display the version of system and command used,
  ..   it would help the user diagnose difference in behavior accross
  ..   seemingly similar system.

  - Suppress *get_command()* and *get_output()*, make turn *takewhile*
    public,

- **IReporter**

  - When bailing out, it is not true that all test passed,

  - Differentiate the error (command aborted) and failure (output
    differs) in the report. Do not bailout on expected return value
    different from zero,

  .. - Explicit manipulation of CommandOutput instance outside the
  ..   reporter instance (report instance should know less about command
  ..   outputs)

  .. - The *str(CommandOutput)* is surprising sometimes, especially the
  ..   returncode shown after a comma,

- **ICommandRunner**

  - Make it possible to follow the session interactively (via cmds.py,
    GNU screen, or via tty). This means being able to read the
    tutorial text paragraph, then *confirm next command*, *abort
    execution*, *take control of the shell*...
 
  - It should be possible to put more than one ellipsis (``...``) per
    line (how does :mod:`doctest` do anyway?),

- **IBlockSelector**

  - Execute not at *parsing* time but at *doctree resolved* time, it
    allows to build a data structure of *articles* and *cleanup
    command* instead of communicating via a flat file descriptor. 

    But it is slower since *wordish* would be blocked until the end of
    parsing and resolution,

  - Support other format syntax, like markdown,

  - Support an INodeSelector( doctree_node ) -> boolean, instantiating
    a *is_shell()*, *is_article()*, *is_cleanup()*. Making it possible
    to gather the snippets in the following data structure::

      # essence  = [ n for n in doctree.traverse()    
      #             if is_article(n) or is_cleanup(n) or is_shell(n) ]   
      # snippets = [ split(a, is_cleanup ) for a in split( essence, is_article ) ]
