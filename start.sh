#!/bin/sh
# start.sh -- launch script
# first, generate the /configs/config.yaml
# second, start clash

if [ ! -f /configs/config.yaml ]; then
    python3 -m clashtools --path /configs/config.yaml --url $SUB_URL
fi

clash -d /configs