# -*- coding: utf-8 -*-
#######################
# tools.tools
#######################

import glob
import os
import yaml

CONFIGS_DIR=os.path.join(os.getcwd(),"etc")
DEP_DB_DIR=os.path.join(CONFIGS_DIR,"dep_db")
DEP_DB_CONF=os.path.join(DEP_DB_DIR,'dbinfo.cfg')

def make_inventory_config():
    pass


def write_inventory_config(filename,config):
    """Dump generated configuration to a file.

    :param filename: ``str`` The filename which to write to.
    :param config: ``dict`` Dictionary containing the config which to write.
    """
    with open(os.path.realpath(filename),'w') as f:
        f.write(yaml.dump(config,default_flow_style=False))
