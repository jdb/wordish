

from distutils.core import setup
import wordish

setup(

    py_modules = [ 'wordish' ],

    name = 'wordish',
    version = '1.0.0beta4',
    author = 'Jean Daniel Browne',
    author_email = 'jeandaniel.browne@gmail.com',
    description = ("Parses a shell session, execute the "
                   "commands, compare the outputs, build a report"),

    url = 'http://jdb.github.com/wordish/',
    long_description = """
Wordish is a script which executes a shell session parsed from a
documentation in the restructured text [#]_ format, then tests and builds a
report of the execution. To mark up shell code in an article,
*wordish* uses the custom directive ``sourcecode``, with the required
argument ``sh``. When presented with an article:

#. *wordish* filters out the text which is not marked with
   ``sourcecode``,

#. then, separates the blocks of shell codes between *commands* and
   *outputs*: 

   #. *wordish* consumes the prompt, parses for the newline which ends
      command,

   #. then parses for the prompt which ends the output, 

Example::

  .. sourcecode:: sh

     ~$ echo "hello world"   # Mmmh, insightful comment
     hello world

This simply renders like:

::

   ~$ echo "hello world"   # Mmmh, insightful comment
   hello world

The *command* starts after the prompt ("~$ ") and continues until the
first newline is found in the source code block. Here, it is just
after the word ``comment``. The command is ``echo "hello world" # Mmmh,
insightful comment`` The output is the text block found until the next
prompt: this is ``hello world``. There are **two** possible prompts:
``~$``, and ``~#``. Both are required to be followed by a space are are
treated the same.

Note: the newlines which are nested in curly brackets or parentheses are
**not** interpreted as an *end of command* character. Shells do the same:
curly brackets are used to define functions and parentheses makes the
nested command to be interpreted in a subprocess shell. The two
following examples from the introduction make it clear:

::

   ~$ (
   echo $((1+1)) )
   2

   ~$ sum () {
   echo $(( $1 + $2 ))
   }

The first command is ``echo $((1+1))`` in a subproces, and it's output
is ``2``. The second command is the definition of a function named
``sum`` and has no output. Defining functions sometimes clarify the
intent in subsequent uses of the function. For functions to be re-used,
the state of the shell must be kept between each snippets. *wordish*
keep a connection with the same *shell* subprocess (*bash* is used)
for the duration of the article.

::

   ~$ sum 42 58
   3

See how the output is obviously incorrect? we will see later how this
is reported.

When the output can not be completely predicted, such as when
displaying ``$RANDOM``, or displaying the size of a partitions in
bytes, there is a handy wildcard pattern which can be used:
``...``. It matches everything like ``.*`` in regexp [#]_.

::

   ~$ echo "a random number: " $RANDOM
   ...

One last thing, if a command does not exit gracefully, *wordish*
precautiously aborts, refusing to execute commands on the system under
test which is in an undefined state. *wordish* displays the remaining
unexecuted commands.

::

   ~$ What have the Romans ever done for us
   aqueduct? roads? wine !

   ~$ echo "Bye bye"
   Bye bye

This introduction is embedded in the wordish module as the
docstring. Just run *wordish* with no argument to get the example
report of this article:

::

   ~$ python -m wordish
   Trying:	echo "hello world"   # Mmmh, insightful comment...
   Expecting:	hello world
   ok
   
   Trying:	(
   echo $((1+1)) )
   Expecting:	2
   ok
   
   Trying:	sum () {
   echo $(( $1 + $2 ))
   }
   Expecting:	
   ok
   
   Trying:	sum 42 58
   Expecting:	3
   Failed, got:	100, 0
   
   Trying:	echo "a random number: " $RANDOM
   Expecting:	...
   ok
   
   Trying:	What have the Romans ever done for us
   Expecting:	aqueduct? roads? wine !
   Failed, got:	/bin/bash: line 19: What: command not found, 127
   
   Command aborted, bailing out
   Untested command:
   	echo "Bye bye"
        python -m wordish
   6 tests found. 
   4 tests passed, 2 tests failed.

There is another example real world article_ which is also included in
the sources distribution, and tested before each release. This is the
article which prompted the need for the development of *wordish*.

.. _article: http://jdb.github.com/sources/lvm.txt

.. [#] This syntax can be seen as light and readable version of html
       or latex, and was designed with the experience of existing Wiki
       syntaxes. The Sphinx project has a nice introduction_ on *rst*,
       the reference documentation is here_.

       .. _introduction: http://sphinx.pocoo.org/rest.html

       .. _here: http://docutils.sourceforge.net/rst.html#user-documentation

.. [#] Regexp are not directly used so that the various special regexp
       characters do not need to be escaped.

""",


    license = 'GPL',

    requires = [ 'docutils (>=0.5)' ],

    classifiers = [ 'Development Status :: 4 - Beta',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'Intended Audience :: Education',
                    'Intended Audience :: System Administrators',
                    'License :: OSI Approved :: GNU General Public License (GPL)',
                    'Operating System :: Unix',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Unix Shell',
                    'Topic :: Documentation',
                    'Topic :: Education',
                    'Topic :: Software Development :: Testing',
                    'Topic :: Utilities']
    )
