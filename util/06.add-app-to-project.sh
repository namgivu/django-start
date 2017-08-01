#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s

#load input
source "$SCRIPT_HOME/common-input.sh"


#add app to the project
echo "
Add a new entry at 'mysite/mysite/settings.py' at INSTALLED_APPS dict
Entry = path to app config file e.g. 'polls.apps.PollsConfig'
"
