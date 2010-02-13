

from distutils.core import setup
import wordish

setup(

    py_modules = [ 'wordish' ],

    name = 'wordish',
    version = '1.0.0beta',
    author = 'Jean Daniel Browne',
    author_email = 'jeandaniel.browne@gmail.com',
    description = ("Parses a shell session, execute the "
                   "commands, compare the outputs, build a report"),

    long_description = wordish.__doc__,

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
