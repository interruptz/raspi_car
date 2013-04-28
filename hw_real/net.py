#!/usr/bin/env python 

import os
import socket 

WIFI_DEVICE = 'wlan0'
WIFI_AP_NAME = 'nerds-guest'
WIFI_AP_PASS = 'nerds'

# util
def osystem(s):
    return os.system(s + ' > /dev/null')
def net_available():
    return osystem('ping -c 1 -W 1 8.8.8.8') == 0
def net_ip():
    return socket.gethostbyname(socket.gethostname())

# Wifi Specific.
def wifi_on():
    osystem('ifconfig %s up' % (WIFI_DEVICE,))
def wifi_off():
    osystem('ifconfig %s down' % (WIFI_DEVICE,))
    kill_dhcpcd(WIFI_DEVICE)
def kill_dhcpcd(ifname):
    if os.path.exists('/run/dhcpcd-%s.pid' % (ifname, )):
        osystem('kill -9 `cat /run/dhcpcd-%s.pid`' % (ifname,))
def wifi_connect():
    # TODO Auto detect 
    cmd = 'iwconfig %s essid "%s" key "s:%s"' % (WIFI_DEVICE, WIFI_AP_NAME, WIFI_AP_PASS)
    osystem(cmd)
    kill_dhcpcd(WIFI_DEVICE)
    cmd = 'dhcpcd %s' % (WIFI_DEVICE,)
    osystem(cmd)
    return net_available() 
