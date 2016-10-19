#!/usr/bin/python

#region import yihabapar utility
import sys, os
UTIL_HOME='{APP_HOME}/util'.format(APP_HOME='%s/..' % os.path.abspath(os.path.dirname(__file__)) )
sys.path.insert(0, UTIL_HOME)
from util_init import *
#endregion import yihabapar utility

gitRepo = {
  'url'    : 'git@github.com:namgivu/yihabapar.git',
  'branch' : 'master',
  'key'    : '/home/ubuntu/.ssh/namgivu-github-ssh',
}
CLONED_TO_DIR='/tmp/namgivu'
CLONED_TO_NAME='yihabapar'

git_clone(gitRepo, CLONED_TO_DIR, CLONED_TO_NAME)