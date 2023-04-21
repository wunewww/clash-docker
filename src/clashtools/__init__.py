#!/bin/env python3
'''
clashtools -- a toolset for clash

The package include several useful functions and variables
for configuring clash.
'''
import os

SUB_URL = os.environ['SUB_URL']
CONF_PATH = '.'
SUB_PROXY = os.environ.get('SUB_PROXY', None)