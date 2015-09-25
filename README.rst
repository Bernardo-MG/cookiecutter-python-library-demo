================================
Cookiecutter Python Library Demo
================================

This is a project created with the `Cookiecutter Python Library
<https://github.com/Bernardo-MG/cookiecutter-python-library>`_ template and
ready to be used for creating a new Python library.

Just check the readme and docs, to adapt them to your project, and it is done.

Remember that if you want to create a new project it is better just reusing
the Cookiecutter Python Library template, as this will set up the initial
project according to a few pieces of data it will ask for.

.. image:: https://badge.fury.io/py/cookiecutter-python-library-demo.svg
    :target: https://pypi.python.org/pypi/cookiecutter-python-library-demo
    :alt: Cookiecutter Python Library Demo Pypi package page

.. image:: https://readthedocs.org/projects/cookiecutter-python-library-demo/badge/?version=latest
    :target: http://cookiecutter-python-library-demo.readthedocs.org/en/latest/
    :alt: Cookiecutter Python Library Demo latest documentation Status
.. image:: https://readthedocs.org/projects/cookiecutter-python-library-demo/badge/?version=develop
    :target: http://cookiecutter-python-library-demo.readthedocs.org/en/develop/
    :alt: Cookiecutter Python Library Demo development documentation Status

Features
--------

By default the project comes with the following features:

- Travis configuration file
- Customized setup.py module to minimize configuration, and using tox for the tests
- Docs using `Sphinx`_ and the `Sphinx Docs Theme <https://github.com/Bernardo-MG/sphinx-docs-theme>`_
- Prepared to run tests through tox
- Prepared to run tests on Python 2.6, 2.7, 3.2, 3.3, 3.4
- Prepared to run tests on pypy and pypy 3
- Prepared to run tests on Jython
- Prepared to run coverage tests and integrate with `Coveralls <https://coveralls.io>`_
- Prepared to run tests for the `Sphinx`_ documentation

Documentation
-------------

Check the `latest docs`_ for the most current version of the documentation.

You can also create the documentation from the source files, kept in the 'docs'
folder, with the help of Sphinx. For this use the makefile, or the make.bat
file, contained on that folder.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 2.6
- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4
- Pypy
- Pypy 3
- Jython

All other dependencies are indicated on the requirements.txt file.
The included makefile can install them with the command:

``$ make requirements``

Installing
~~~~~~~~~~

The project is offered as a `Pypi package`_, and using pip is the preferred way
to install it. For this use the following command;

``$ pip install cookiecutter-python-library-demo``

If manual installation is required, the project includes a setup.py file, along
a makefile allowing direct installation of the library, which can be done with
the following command:

``$ make install``

Usage
-----

The application has been coded in Python, without using any particular
framework.

Collaborate
-----------

Any kind of help with the project will be well received, and there are two main ways to give such help:

- Reporting errors and asking for extensions through the issues management
- or forking the repository and extending the project

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues tracker`_, where any Github
user may report bugs or ask for new features.

Getting the code
~~~~~~~~~~~~~~~~

If you wish to fork or modify the code, visit the `GitHub project page`_, where
the latest versions are always kept. Check the 'master' branch for the latest
release, and the 'develop' for the current, and stable, development version.

License
-------

The project has been released under the `MIT License`_.

.. _GitHub project page: https://github.com/Bernardo-MG/cookiecutter-python-library-demo
.. _latest docs: http://cookiecutter-python-library-demo.readthedocs.org/en/latest/
.. _Pypi package: https://pypi.python.org/pypi/cookiecutter-python-library-demo
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
.. _project issues tracker: https://github.com/Bernardo-MG/cookiecutter-python-library-demo/issues
.. _Sphinx: http://sphinx-doc.org/
