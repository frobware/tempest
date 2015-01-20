#!/usr/bin/env bash

basedir=$(dirname "$(readlink -f "$0")")

set -o pipefail

TESTRARGS=$1
nlines=${TOX_PROGRESS_NLINES:-$(testr list-tests | wc -l)}
python setup.py testr --testr-args="--subunit $TESTRARGS" | subunit-trace --no-failure-debug -f | python -u "$basedir"/tox-progress.py --print-date --nlines=$nlines
retval=$?
# NOTE(mtreinish) The pipe above would eat the slowest display from pbr's testr
# wrapper so just manually print the slowest tests.
echo -e "\nSlowest Tests:\n"
testr slowest
exit $retval
