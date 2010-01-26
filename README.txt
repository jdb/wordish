

=========
 wordish
=========


Shells are applications often used by administrators or developers
to carry out very diverse type of operations: the list is virtually
boundless and includes, for example, disk management, network
administration, source code version control, or application packaging
and deployment. Documentation of shell operations are eased by the
fact that a shell session is composed of text commands and outputs,
which is easy to copy and paste, or to present orderly.

Wordish is a project which parses a shell session from a documentation
which contains the commands and the expected output, and verifies that
they work exactly as shown, to make sure the documentation is
correct. For example, if the file hello.txt is laid out like::

  ~$ cat hello.txt
  echo "Hello World"
  Hello World

The shell session can be test with::

  ~$ python -m wordish hello.txt

The report will show::
  Trying:       echo "hello world"
  Expecting:    hello world
  ok

  1 tests found. 
  All tests passed

*Wordish can test wordy shell articles*

Administrators will found more details in the *How to test an article*
and in *How to write an article* paragraphs.

Anyone curious of how this is designed may be interested the *Object
model and interfaces*. 

For the brave Python developper which is impatient to propose a
feature patch, a bug report and fix, the *Source presentation*,
*Test suite* and the *Wordish versions and packages* may be
helpful. 

The author of these lines must say that he finds that *unit testing*
and *packaging* are still black magic and would be grateful for the
reader's advice and response to the many existential questions listed
*here* and *there*


How to test an article
======================

Installation
------------

Wordish is available on the Python package index. Provided the
setuptools package is installed, ``wordish`` can be installed with::

  easy_install wordish

At this point the wordish command is available from the shell.

The python module is copied in the Python path ( in sites-packages/ on
Debian), and the ``wordish`` command is copied in the path, in
``/usr/local/bin``.

Debian packages and RPM will be available.


the ``wordish`` command and options
-----------------------------------


Examples
--------


        readme
        man
        wordish --help
        presentation
        installation and verification


How to write an article
=======================

        parsing method (prompts, nesting)
        matching methods (ignoring, ellipsis, re)
        one subshell for the session
        working examples: raid, lvm, deb, git, ssh, ipvsadm


Object model and interfaces
===========================

Overview
--------

There is a ShellSessionParser, a output which of stdout, stderr, the
returncode and

Wordish makes use of five python modules nothing else than shlex,
itertools, :mod:`StringIO` which adapts a character string to the
interface open file. and and sys

parser
------

output
------

runner
------

reporter
--------

Sources presentation
====================

        parser
        output
	runner
        reporter

tests
=====


        refactor the tests
            some are harmful for readability
            some are not useful
            some pertinent tests are missing
            some should doctest instead of unittest and vice versa
            distinction should be made between testing the public api and the rest
            have I used backdoors?
            are interface tested?
            am i white box or black box
            how to put the simple session and the git howto in the test_wordish


Versions and packaging
======================

        source, branches and versions
        packaging
	documentation


limitations, roadmap and crazy ideas
====================================

        setup.py and entry point
        rst builder, sphinx builder
        doctests to unittests
        quiet mode without output
        universal linefeed for commands in win articles
        list commands used and version
        at bailout, show rest to help cleanup and help debug
        interactive via cmds.py or screen (tty?), confirm, insert command, ctrl-C ...
        executable script with #!/usr/bin/bash
        other parsing format, markdown
        hints in a command's comments
            ignore
            input
            &2
