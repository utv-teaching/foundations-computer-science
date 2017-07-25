#!/usr/bin/env bash

_PWD=$(pwd)

cd "$(dirname "${BASH_SOURCE[0]}")"

JARS=$(bash list-jars.sh)

java -Xmx512m -Dpython.home="jython-2.2.1" -Dpython.cachedir="$HOME/.jes-cachedir " -classpath ".:$JARS:Sources:$CLASSPATH" JESstartup

cd $_PWD
