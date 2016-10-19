#!/usr/bin/python
'''
test util from yihabapar project ref. https://github.com/namgivu/yihabapar
'''

#region import yihabapar utility
import sys, os
UTIL_HOME='{APP_HOME}/util'.format(APP_HOME='%s/..' % os.path.abspath(os.path.dirname(__file__)) )
sys.path.insert(0, UTIL_HOME)
from util_init import *
#endregion import yihabapar utility

run_bash('echo yihabapar')

run_bash('{APP_HOME}/sandbox/test-get_arg.py {arg01} {arg02}'.format(
  APP_HOME=APP_HOME,
  arg01=122,
  arg02='abb')
)
