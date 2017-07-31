#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s

#load input
source "$SCRIPT_HOME/common-input.sh"

#ref. https://docs.djangoproject.com/en/1.11/intro/tutorial01/#creating-a-project
curd=`pwd` ; cd $CODE_HOME
django-admin startproject "$PROJECT_NAME"
cd $curd

#conclusion
echo "
Project '$PROJECT_NAME' created at '$PROJECT_HOME'
"
