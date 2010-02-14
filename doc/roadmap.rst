
.. _roadmap:

Roadmap: current limitations and future ideas
=============================================

objects and interfaces
----------------------

- **ISessionParser**

  - *Universal* linefeed for commands in articles written on Windows, 

  - Like doctest, write hints for wordish to adjust its behavior when
    parsing hints in the comment after a command::

       ~$ echo boilerplate      # ignore
       unpredictable

       ~$ echo coucou >&2       # &2
       coucou

       ~$ She is a witch        # returncode: 127
       She: command not found

       ~$ rm -r ./temp_mount_point   # cleanup

    The returned expected could be an CommandOutput instead of simple
    string and carry the attribute *ignore*, *returncode*, *cleanup*
    or *err*.

  .. - If *wordish* could display the version of system and command used,
  ..   it would help the user diagnose difference in behavior accross
  ..   seemingly similar system.

  .. - Suppress *get_command()* and *get_output()*, make turn *takewhile
  ..   public*,

- **IReporter**

  - When bailing out, it is not true that all test passed,

  - Differentiate the error (command aborted) and failure (output
    differs) in the report. Be able to expect return value different
    from zero,

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
    line (how does doctest do anyway?),

- **IBlockSelector**

  - Execute not at *parsing* time but at *doctree resolved* time, it
    allows to structure the input in *article* and *cleanup* instead
    of a flat file descriptor. But it is slower since *wordish* would
    be blocked until the end of parsing and resolution,

  - Support other format syntax, like markdown,

  - Support an INodeSelector( doctree_node ) -> boolean, instantiating
    a *is_shell*, *is_article*, *is_cleanup* ::

      # essence  = [ n for n in doctree.traverse()    
      #             if is_article(n) or is_cleanup(n) or is_shell(n) ]   
      # snippets = [ split(a, is_cleanup ) for a in split( essence, is_article ) ]


Python/debian packaging
-----------------------

- use *distribute* to benefit from ``console_script``, and dependency
  resolution (docutils), and also because it is the new black. Maybe
  *pip* knows how to handle man pages (and re-hash the man-db),

- functional at the docutils level but how to package the future
  *sphinx.ext.wordish* (should the repository be on bitbucket),

- command line argument: ``--help``, ``--quiet``, ``--prompt``,
  ``--match 'exact|ellipsis|regexp'``, ``--cleanup mycleanup.sh``,
  ``ignore_stderr``, ``bailout_on_abort``

- how to use git branches to ease debian and rpm packaging?

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
  *iterable*, that a member attribute is a list or a dictionary,

- Use epydoc, or Sphinx syntax to specify the signature of methods and
  objects

Tests
-----

- some impede readability, some are redundant, some use backdoors,
  some pertinent tests are missing, some doctest would better be unit
  test and vice versa,

- clear distinction between public (black box) and private api (white
  box) (test the public at least),

- some black box may need to be launched as root and be run on every
  file in *example/*,

Integration with Sphinx
-----------------------

- Sphinx integration, how to to reuse ``sourcecode``, so that it has an
  ``ignored``, ``cleanup option``, ``no_check``, ``can_abort``,

- configuration: bailout_on_abort, match=string,re,ellipsis, prompts,
  ignore_stderr, 

- use the logging system which can be shut from the command line,

- build a directive ``test_report`` inserting the report in the doc,        

- build a directive ``article`` which takes the name of the article,
  and for each, creates a command runner and accumulate the cleanup
  code, in case of an abort


.. pr plan
..     shunit
..     lo lange
..     ubuntu
..     sphinx
..     docutils
..     lvs
..     guy from redhat
..     debian administration
..     python planet
..     debian planet
..     debian ml
..     anevia
..     roming
..     imil
