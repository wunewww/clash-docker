#!/bin/sh
# start.sh -- launch script
# first, generate the /configs/config.yaml
# second, start clash

cd /src
python3 -m clashtools --path /configs/config.yaml --url $SUB_URL

clash -d /configs