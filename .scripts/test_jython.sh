#!/bin/bash
# This script runs the tests using Jython
#
# It makes use of Pyenv to set up the interpreter
#
# The following environmental variables are used:
# - JYTHON: boolean, control flag for running the tests, should be true to run these tests

if [ "$JYTHON" == "true" ]; then

    # Sets up Pyenv
    git clone https://github.com/yyuu/pyenv.git ~/.pyenv
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"

	# Installs Jython
    echo "Installing Jython"
    pyenv install jython-2.7.0
    pyenv local jython-2.7.0

    eval "$(pyenv init -)"

    echo "Interpreter version:"
    python --version

    echo "Running tests"
    jython -m pip install -rrequirements.txt
    jython -m pip install pytest

	# Runs tests
    jython -m py.test

fi
