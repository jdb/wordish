

from distutils.core import setup

setup(

    py_modules = [ 'wordish' ],

    name = 'wordish',
    version = '0.0.6',
    author = 'Jean Daniel Browne',
    author_email = 'jeandaniel.browne@gmail.com',
    description = ("Parses a shell session, test the "
                   "commands compare the outputs"),

    long_description = """
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
correct. 

For example, if the file hello.txt is laid out like::

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
""",
    classifiers = [ 'Development Status :: 3 - Alpha',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'Intended Audience :: Education',
                    'Intended Audience :: System Administrators',
                    'License :: OSI Approved :: GNU General Public License (GPL)',
                    'Operating System :: Unix',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Unix Shell',
                    'Topic :: Documentation',
                    'Topic :: Education',
                    'Topic :: Software Development :: Testing',
                    'Topic :: Utilities'],

    license = 'GPL'

    )
