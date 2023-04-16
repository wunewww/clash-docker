#!/bin/sh
# this script find the container's ip address of interface eth0
ip addr show eth0 | egrep -o "172\.17\.[0-9]{1,3}\.[0-9]{1,3}" | head -n 1
