
.. _write:

How to write an article
=======================

The article should be written in restructured text syntax. This syntax
can be seen as light and readable version of html or latex, and was
designed with the experience of existing Wiki syntaxes. The Sphinx
project has a nice introduction_ on *rst*, the reference documentation
is here_.

.. _introduction: http://sphinx.pocoo.org/rest.html

.. _here: http://docutils.sourceforge.net/rst.html#user-documentation

To display shell code in an article, Sphinx uses the custom directive
``sourcecode``, that *wordish* has adopted too. When presented with an
article, it is an easy step to filter out the text which is not marked
with ``sourcecode``, then to differentiate between *commands* and
*outputs*, *wordish* parses for the newline which ends command and for
the prompt which end output ::

   A very short article  
   
   .. sourcecode:: sh
   
      ~$ echo "She is a witch!"
      She is a witch!
  
   Really interesting indeed !  

The first newline in the source code block, is found just after the
quotation mark: it delimites the command which started after the
prompt. The output is the text block found until the next prompt.
There are two possible prompts: ``~$``, and ``~#``. Both are 
required to be followed by space. 

Note: the newlines which are nested in curly brackets or parentheses are
not interpreted and an *end of command* character. Shell do the same,
curly brackets are used to define functions and parentheses makes the
nested command to be interpreted in a sub process shell. The two
following examples from the introduction make it clear::

   .. sourcecode:: sh

      ~$ (
      echo $((1+1)) )
      2

      ~$ sum () {
      echo $(( $1 + $2 ))
      }

The first command is ``echo $((1+1))`` in a subproces, and it's output
is ``2``. The second command is the definition of a function named
``sum`` and has no output.

When the output can not be completely predicted, such as when
displaying ``$RANDOM`` as in the introduction, or displaying the
content of the partitions file in */proc*, there is a handy wildcard
pattern which can be used: ``...``. It matches everything like ``.*``
in regexp [#]_.

The state of the shell is kept between each snippets. This means, for
instance, that when declaring a function in a snippet like ``sum``
above, can be used in the subsequent snippets of an article [#]_.

There is another example article_, also included in the sources
distribution, and tested before each release. This is the article
which prompted the need for the development of *wordish*.

.. _article: http://jdb.github.com/sources/lvm.txt

.. [#] Regexp are not directly used so that the various special regexp
       characters do not need to be escaped
       
.. [#] A naive way to execute command is is to use :func:`system` to
       execute a shell command, *wordish* does not do this and keep a
       connection with a shell subprocess for the duration of the
       article
