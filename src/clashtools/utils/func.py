'''
func.py

Define some useful functions to configure clash
'''

import json
import re
from urllib.parse import unquote, urlparse, parse_qs
from ipaddress import IPv4Network, IPv6Network, AddressValueError
import base64
import logging

import yaml
import requests as r

def read_yaml(path: str) -> dict:
    '''
    read_yaml: read the content in `path` into a list.
    '''
    with open(path, "r", encoding="utf-8") as f:
        file_content = f.read()
        logging.debug(f"Read {path} successfully.")
        result = yaml.load(file_content, Loader=yaml.SafeLoader)
        logging.debug(f"Parse yaml file {path} successfully.")
    return result

def write_yaml(path: str, dct: dict) -> None:
    '''
    write_yaml: write dictionary `lst` into `path`
    '''
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(dct, f)
    logging.debug(f"Write to {path} successfully.")
    
def get_url(g_url: str) -> str:
    '''
    get_url: get string content from t_url
    '''
    c = r.get(url=g_url)
    logging.info(f"GET {g_url} successfully.")
    return c

def put_url(p_url: str, obj: dict, q: dict = None) -> None:
    '''
    put_url: PUT dict obj to p_url
    '''
    c = r.put(p_url, data=json.dumps(obj), params=q)

    c.raise_for_status()
    logging.debug(f"PUT data to {p_url} successfully.")

def patch_url(p_url: str, obj: dict) -> None:
    '''
    patch_url: PATCH dict obj to p_url
    '''
    c = r.patch(p_url, data=json.dumps(obj))
    
    c.raise_for_status()
    logging.debug(f"PATCH data to {p_url} successfully.")

def decode_base64(s: str) -> str:
    '''
    decode base64 string s
    '''
    return base64.b64decode(s).decode('utf-8')

def get_subscriptions(l: str) -> str:
    '''
    GET str, return a list of subs (link)
    '''
    logging.debug("Start getting the subscriptions.")
    c64 = get_url(g_url=l)
    logging.debug(f'get content:{c64.text}')
    c = decode_base64(c64.text)
    return c

def parse_clash_subformat(s: str) -> dict:
    '''
    parse s into a dict which key fit clash conf
    '''
    pr = urlparse(unquote(s))
    return {
        "type": pr.scheme,
        "password": pr.netloc.split("@")[0],
        "server": pr.netloc.split("@")[1].split(":")[0],
        "port": pr.netloc.split("@")[1].split(":")[1],
        "sni": parse_qs(pr.query)['sni'][0],
        "name": pr.fragment
    }

def generate_proxies(url: str) -> list:
    '''
    get the decoded proxies link
    '''
    content= get_subscriptions(url).split()
    return [parse_clash_subformat(i) for i in content]

def broke_wildcard(i: str) -> set:
    '''
    get urls and rule from the wildcard type url,
    since the free version of clash doesn't support wildcard in rules
    '''
    pattern = r'^\+\.(.*)'
    if_wildcard = re.match(pattern, i)
    if if_wildcard:
        return [if_wildcard.group(1), 'suffix']
    try:
        IPv4Network(i)
        return [i, 'ipv4']
    except AddressValueError:
        try:
            IPv6Network(i)
            return [i, 'ipv6']
        except AddressValueError:
            return [i, 'domain']