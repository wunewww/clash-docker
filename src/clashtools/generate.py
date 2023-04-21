#!/bin/env python3
'''
generate.py

This file contains functions generate conf
'''
from .defaults import CONF_TEMPLATE, POSITIVE
from .func import generate_proxies, get_url, broke_wildcard
import yaml

def generate_conf(url: str, proxy: dict, use_rule: list = POSITIVE):
    conf = CONF_TEMPLATE
    proxies = generate_proxies(url, proxy)
    conf.update({'proxies': proxies})
    proxy_names = [j['name'] for j in proxies]
    conf.update({
        'proxy-groups': [{
            'name': 'PROXY',
            'type': 'url-test',
            'proxies': proxy_names,
            'url': 'https://google.com',
            'interval': 300
            }]
        })

    rule_set = [rule for i in use_rule for rule in generate_rules(i, proxy)]

    conf.update(
        {
            'rules': rule_set
        }
    )
    return conf

def generate_rules(url_r: list, proxy: dict) -> list:
    t = get_url(url_r[0], proxy)
    y = yaml.load(t.text)
    result = []
    for i in y['payload']:
        broken_down = broke_wildcard(i)
        if broken_down[1] == 'suffix':
            rule = 'DOMAIN_SUFFIX'
        elif broken_down[1] == 'domain':
            rule = 'DOMAIN'
        elif broken_down[1] == 'ipv4':
            rule = 'IP-CIDR'
        elif broken_down[1] == 'ipv6':
            rule = 'IP_CIDR6'
        result.append(f'{rule},{broken_down[0]},{url_r[1]}')
    return result