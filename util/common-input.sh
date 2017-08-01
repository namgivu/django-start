#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s
c="$SCRIPT_HOME/.." ; c=$(cd "$c" && pwd) ; export CODE_HOME=$c

#region echo with color ref. http://stackoverflow.com/a/5947802/248616
HL='\033[1;33m' #high-lighted color
CM='\033[0;32m' #comment color
ER='\033[0;31m' #red color
EC='\033[0m'    #end coloring
#endregion echo with color


PROJECT_NAME='mysite'
PROJECT_HOME="$CODE_HOME/$PROJECT_NAME"
PROJECT_MANAGE="$PROJECT_HOME/manage.py"

APP_POLL='polls'
