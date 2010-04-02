
Packaging
=========

Packaging is meant to facilitate the software deployment. Different
audiences participate in this step of the software lifecycle:

- *Users* have simple standard ways to select and install packages
  adapted to their system.

- Tools are available for *admins* gather packages on centralised
  repositories, or to audit the installed versions and control
  upgrades.

- With a correct package, the Python software can be stored on a
  public repository: the python Package Index.

  The *developer* can define how the software is installed on the user
  system which reduces an important sources of problem: installation
  which does not replicate the developer set up. The package also
  defines how the sources are compiled in the case of Python
  extensions.




Python packaging
----------------

For a Python developer there are many features available by writing a
simple script called setup.py using the *distutils* module from the
standard library:

- Python packages can be stored on the Python Package Index. 

- 



OS package
----------

Operating systems already have their own packaging systems, Debian,
Red Hat as well as Gentoo and 
