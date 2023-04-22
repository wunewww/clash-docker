#!/bin/env python3
'''
__main__.py

run clashtools as module
'''

from .__init__ import generate_conf
from yaml import dump
import logging
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', nargs=1)
    parser.add_argument('--path', nargs=1)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    configuration = generate_conf(args.url[0])
    with open(args.path[0], 'w') as f:
        dump(configuration, f, encoding='utf-8', allow_unicode=True)
