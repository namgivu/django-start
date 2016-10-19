#!/usr/bin/python

#region import yihabapar utility
import sys, os
UTIL_HOME='{APP_HOME}/util'.format(APP_HOME='%s/..' % os.path.abspath(os.path.dirname(__file__)) )
sys.path.insert(0, UTIL_HOME)
from util_init import *
#endregion import yihabapar utility

ext_clone(gitRepo={'url': 'git@github.com:hoangphuong/personal_robot_abilities.git',
                   'branch': 'master',
                   'key': '/home/ubuntu/.ssh/namgivu-github-ssh',
                   },
          CLONED_TO='ext/hoangphuong.maya')
