#!/bin/bash
# This script runs the normal tests
#
# It will build the correct Python interpreter version to test from the
# PYTHON_VERSION variable. As this is meant to be used with Travis this variable
# should store the interpreter's version.
#
# The following environmental variables are used:
# - PYTHON_VERSION: string, stores the version of the Python interpreter to run the tests

tox -e $(echo py$PYTHON_VERSION | tr -d . | sed -e 's/pypypy/pypy/')
