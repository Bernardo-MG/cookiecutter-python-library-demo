#!/bin/bash
# This script runs the coverage tests
#
# The following environmental variables are used:
# - COVERAGE: boolean, control flag for testing, should be true to run tests

if [ "$COVERAGE" == "true" ]; then

    tox -e coverage

fi
