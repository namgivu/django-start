import os, sys

#region path
UTIL_HOME  =os.path.abspath(os.path.dirname(__file__))
COMMON_UTIL=os.path.abspath("%s/common" % UTIL_HOME)
VAULT_HOME =os.path.abspath("%s/vault" % UTIL_HOME)
UTIL_CONFIG=os.path.abspath('%s/util_config.py' % UTIL_HOME)
UTIL_CONFIG_TEMPLATE=os.path.abspath('%s/util_config.template.py' % UTIL_HOME)
#endregion path


#region load util config
if not os.path.exists(UTIL_CONFIG):
  run_bash('cp -f {UTIL_CONFIG_TEMPLATE} {UTIL_CONFIG}'.format(UTIL_CONFIG=UTIL_CONFIG,
                                                               UTIL_CONFIG_TEMPLATE=UTIL_CONFIG_TEMPLATE))
from util_config import util_config
#endregion load util config


#region common helpers
sys.path.insert(0, COMMON_UTIL)
from run_bash import run_bash
from get_arg import get_arg
#endregion common helpers


#region app-specific
APP_NAME = util_config['APP_NAME']
APP_HOME = util_config['APP_HOME']
#endregion app-specific
