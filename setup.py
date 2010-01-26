

from distutils.core import setup

setup(
    py_modules = [ 'wordish' ],
 
    # it seems that I am putting in the source package the debian convention
    data_files = [ ('share/doc/python-wordish/examples',
                    ['examples/lvm_example.txt',] ) ]

    )
