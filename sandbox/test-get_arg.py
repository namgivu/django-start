#!/usr/bin/python
'''
command line syntax
test-get_arg.py {arg01} {arg02}
'''

#region import yihabapar utility
import sys, os
UTIL_HOME='{APP_HOME}/util'.format(APP_HOME='%s/..' % os.path.abspath(os.path.dirname(__file__)) )
sys.path.insert(0, UTIL_HOME)
from util_init import *
#endregion import yihabapar utility

allArgs = ['arg01', 'arg02']

arg01=get_arg('arg01', allArgs=allArgs)
arg02=get_arg('arg02', allArgs=allArgs)

print '''
sandbox/test-get_arg.py
  arg01: {arg01}
  arg02: {arg02}
'''.format(arg01=arg01, arg02=arg02)