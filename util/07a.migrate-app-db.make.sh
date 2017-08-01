#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s

#load input
source "$SCRIPT_HOME/common-input.sh"

#make migrate file
python $PROJECT_MANAGE makemigrations $APP_POLL
  #run 'makemigrations' to tell Django that the models get updated, and that to create a new migration to record the changes.
  #migrations are files on disk e.g. 'polls/migrations/0001_initial.py'
