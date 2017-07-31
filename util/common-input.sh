#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s
c="$SCRIPT_HOME/.." ; c=$(cd "$c" && pwd) ; export CODE_HOME=$c

PROJECT_NAME='mysite'
PROJECT_HOME="$CODE_HOME/$PROJECT_NAME"

APP_MYSITE=$PROJECT_NAME
APP_POLL='polls'
