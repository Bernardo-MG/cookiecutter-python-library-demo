# -*- coding: utf-8 -*-
import ast
import re
import sys
import io
from os.path import dirname
from os.path import join
from codecs import open

from setuptools import find_packages, setup
from setuptools.command.test import test as test_command

"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Test requirements
_tests_require = ['tox']


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

# Gets the version for the source folder __init__.py file
with open('cookiecutter-python-library-demo/__init__.py', 'rb',
          encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))


class _ToxTester(test_command):
    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox

        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name='cookiecutter-python-library-demo',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=version_lib,
    description='Demo for the Cookiecutter Python Library project',
    author='Bernardo Martínez Garrido',
    author_email='programming@wandrell.com',
    license='MIT',
    url='https://github.com/Bernardo-MG/cookiecutter-python-library-demo',
    download_url='https://pypi.python.org/pypi/cookiecutter-python-library-demo',
    keywords=[],
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'setuptools',
        'sphinx_bootstrap_theme',
        'twine',
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={'test': _ToxTester},
)
