#!/bin/env python3
'''
defaults.py

This file defines some default value used for clashtools

CONF_TEMPLATE -- the default clash configuration of clash
L_DIRECT -- rules of direct connection
L_PROXY -- rules of proxy connection
L_REJECT -- rules of blocking adds
'''

CONF_TEMPLATE = {
    "mixed-port": 7890,
    "allow-lan": True,
    "bind-address": '*',
    'mode': 'Rule',
    'ipv6': True,
    'log-level': 'info',
    'external-controller': "127.0.0.1:9090"
}

L_DIRECT = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt', 'DIRECT']
L_PROXY = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/proxy.txt', 'PROXY']
L_REJECT = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/reject.txt', 'REJECT']
L_PRIVATE = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/private.txt', 'DIRECT']
L_APPLE = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/apple.txt', 'DIRECT']
L_ICLOUD = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/icloud.txt', 'DIRECT']
L_GOOGLE = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/google.txt', 'DIRECT']
L_GFW = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/gfw.txt', 'PROXY']
L_GREATFIRE = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/greatfire.txt', 'PROXY']
L_TLD_NOT_CN = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/tld-not-cn.txt', 'PROXY']
L_TELEGRAMCIDR = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt', 'PROXY']
L_LANCIDR = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/lancidr.txt', 'DIRECT']
L_CNCIDR = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/cncidr.txt', 'DIRECT']
L_APPLICATIONS = ['https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/applications.txt', 'DIRECT']

POSITIVE = [L_PRIVATE, L_REJECT, L_ICLOUD, L_APPLE, L_GOOGLE, L_PROXY, L_DIRECT, L_LANCIDR, L_CNCIDR, L_TELEGRAMCIDR]
NEGATIVE = [L_PRIVATE, L_REJECT, L_TLD_NOT_CN, L_GFW, L_GREATFIRE, L_TELEGRAMCIDR]