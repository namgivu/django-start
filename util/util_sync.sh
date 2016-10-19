#!/usr/bin/env bash

#ref. http://stackoverflow.com/a/246128/248616
SCRIPT_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#let-me-in.sh tool to run syncing
letmein="/home/namgivu/NN/code/yihabapar/let-me-in.sh"
if [ ! -z $1 ]; then
  letmein=$1
fi

sh="$letmein $SCRIPT_HOME"

echo "Utility sync... DONE"
echo
eval $sh
echo
echo $sh
echo "Utility sync... DONE"
