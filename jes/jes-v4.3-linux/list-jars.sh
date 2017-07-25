#!/usr/bin/env bash

WSDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
JARS=""

JARS="$WSDIR/jars/jython.jar"
JARS="$JARS:$WSDIR/jars/jmf.jar"
JARS="$JARS:$WSDIR/jars/jl1.0.jar"
JARS="$JARS:$WSDIR/jars/junit.jar"
JARS="$JARS:$WSDIR/jars/AVIDemo.jar"

echo $JARS