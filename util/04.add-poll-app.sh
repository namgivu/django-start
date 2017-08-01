#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s

#load input
source "$SCRIPT_HOME/common-input.sh"

#ref. https://docs.djangoproject.com/en/1.11/intro/tutorial01/#creating-a-project
curd=`pwd` ; cd $PROJECT_HOME
python $PROJECT_MANAGE startapp $APP_POLL
cd $curd

#conclusion
echo "App '$APP_POLL' created at '$PROJECT_HOME/$APP_POLL' "
