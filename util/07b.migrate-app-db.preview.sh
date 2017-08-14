#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s

#load input
source "$SCRIPT_HOME/common-input.sh"
MIGRATE_NUM=$1
if [ -z "$MIGRATE_NUM" ]; then
  MIGRATE_NUM='0001'
fi


#print sql command
echo ; echo -e "${CM}mysql-run preview @ migration${EC}"
python $PROJECT_MANAGE sqlmigrate $APP_POLL $MIGRATE_NUM

#run health check
echo ; echo -e "${CM}Health check @ migration${EC}"
python $PROJECT_MANAGE check
