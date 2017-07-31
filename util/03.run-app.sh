#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s

#load input
source "$SCRIPT_HOME/common-input.sh"
RUN_PORT=8000
IP_FILTER=0

#ref. https://docs.djangoproject.com/en/1.11/intro/tutorial01/#the-development-server
curd=`pwd` ; cd $CODE_HOME/$APP_NAME
python manage.py runserver $IP_FILTER:$RUN_PORT
cd $curd
