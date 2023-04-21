#!/bin/env python3
'''
__main__.py

run clashtools as module
'''

from .generate import generate_conf
from .__init__ import SUB_URL
from yaml import dump
import logging

proxies_r = {
    "http": 'http://172.26.48.1:8080',
}

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    a = generate_conf(SUB_URL, proxy=None)
    with open("./config", 'w') as f:
        dump(a, f, encoding='utf-8')
