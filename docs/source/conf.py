#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Cookiecutter Python Library Demo documentation build configuration file.

import ast
import re
import sys
import os
import datetime
from codecs import open
from os import path

# -- Version --------------------------------------------------------------

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Path to the project's root
here = path.abspath(path.dirname(__file__))

# Gets the version for the source folder __init__.py file
with open('../../cookiecutter-python-library-demo/__init__.py', 'rb',
          encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))

# -- Code location --------------------------------------------------------

sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('../../cookiecutter-python-library-demo'))


# -- General configuration ------------------------------------------------

# Sphinx extensions
#
# autodoc: generates documentation from docstrings
# intersphinx: generates links to other Sphinx-created docs
# viewcode: generates HTML from code sources
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# Templates.
templates_path = ['_templates']

# Only reStructuredText is accepted
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Sort members by type
autodoc_member_order = 'groupwise'

# General information about the project.
project = 'Cookiecutter Python Library Demo'
project_safe = project.replace(' ', '_')
copyright = u'2015, Bernardo Martínez Garrido'
authors = [u'Bernardo Martínez Garrido']

# The version info for the project.
#
# Semantic version value.
version = version_lib
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

import sphinx_docs_theme

# Activate the theme.
html_theme = 'sphinx_docs_theme'
html_theme_path = sphinx_docs_theme.get_html_theme_path()

# Removes permalink markers
html_add_permalinks = ''

# Theme options.
html_theme_options = {
    'keywords': '',
    'author_name': ','.join(authors),
    'author_url': 'https://github.com/Bernardo-MG',
    'twitter_id': '@Bernardo-MG',
    'publish_date': datetime.datetime.now().date(),
    'scm_name': 'Github',
    'scm_url': 'https://github.com/Bernardo-MG/cookiecutter-python-library-demo',
    'ci_name': 'Travis',
    'ci_url': 'https://travis-ci.org/Bernardo-MG/cookiecutter-python-library-demo',
    'issues_name': 'Github',
    'issues_url': 'https://github.com/Bernardo-MG/cookiecutter-python-library-demo/issues',
    'supported_list': ['Python 2.6', 'Python 2.7', 'Python 3.2', 'Python 3.3',
                       'Python 3.4', 'pypy', 'pypy3'],
    'releases_repos': [
        ('Pypi',
         'https://pypi.python.org/pypi/cookiecutter-python-library-demo')],
    'general_info_links': [('Acquire', './acquire.html'),
                           ('Usage', './usage.html')],
    'navbar_links': [('Documentation', [('Acquire', './acquire.html'),
                                        ('Usage', './usage.html')]),
                     ('Info and Reports', [('Reports', './reports.html')])],
}

# Output file base name for HTML help builder.
htmlhelp_basename = '%s doc' % project

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

# List of LaTeX documents.
latex_documents = [
    (master_doc, '%s.tex' % project_safe, '%s Documentation' % project,
     ','.join(authors), 'manual'),
]


# -- Options for manual page output ---------------------------------------

# List of manual pages.
man_pages = [
    (master_doc, project, '%s Documentation' % project,
     [','.join(authors)], 1)
]


# -- Options for Texinfo output -------------------------------------------

# List of Texinfo documents.
texinfo_documents = [
    (master_doc, project, '%s Documentation' % project,
     ','.join(authors), project, 'Demo for the Cookiecutter Python Library project',
     'Miscellaneous'),
]


# -- Intersphinx links ----------------------------------------------------

# Intersphinx mapping.
intersphinx_mapping = {
    'https://docs.python.org/': None,
}
