#!/bin/env python3
'''
generate.py

This file contains functions generate conf
'''
from .defaults import CONF_TEMPLATE, POSITIVE, NEGATIVE
from .func import generate_proxies, get_url, broke_wildcard, put_url
import yaml
import logging

def generate_conf(url: str, positive=True):
    conf = CONF_TEMPLATE
    logging.info("Start fetch subscriptions.")
    proxies = generate_proxies(url)
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

    if positive:
        rule_set = [rule for i in POSITIVE for rule in generate_rules(i)]
        rule_set.append('GEOIP,LAN,DIRECT')
        rule_set.append('GEOIP,CN,DIRECT')
        rule_set.append('MATCH,PROXY')
    else:
        rule_set = [rule for i in NEGATIVE for rule in generate_rules(i)]
        rule_set.append('MATCH,DIRECT')
        

    conf.update(
        {
            'rules': rule_set
        }
    )
    return conf

def generate_rules(url_r: list) -> list:
    logging.info('Start fetching rule set.')
    t = get_url(url_r[0])
    y = yaml.load(t.text, Loader=yaml.SafeLoader)
    result = []
    for i in y['payload']:
        broken_down = broke_wildcard(i)
        if broken_down[1] == 'suffix':
            rule = 'DOMAIN-SUFFIX'
            result.append(f'{rule},{broken_down[0]},{url_r[1]}')
        elif broken_down[1] == 'domain':
            rule = 'DOMAIN'
            result.append(f'{rule},{broken_down[0]},{url_r[1]}')
        elif broken_down[1] == 'ipv4':
            rule = 'IP-CIDR'
            result.append(f'{rule},{broken_down[0]},{url_r[1]},no-resolve')
        elif broken_down[1] == 'ipv6':
            rule = 'IP-CIDR6'
            result.append(f'{rule},{broken_down[0]},{url_r[1]},no-resolve')
    return result

def reload_clash(url: str, path: str) -> None:
    loads = { 'path': path }
    res = put_url(url, loads)
    res.raise_for_status()