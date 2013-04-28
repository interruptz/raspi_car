#!/usr/bin/env python 

import hw.net as n
import hw.light as l
import time
import os

def start(irc_init, irc_notifier):
    n.wifi_on()
    n.wifi_connect()
    b = irc_init()
    while not b.ready:
        time.sleep(0.1)
    irc_notifier('Connected to an available Wi-Fi network. All systems go!')
    while True:
        time.sleep(60 * 3)
        if not n.net_available():
            n.wifi_off()
            n.wifi_on()
            n.wifi_connect()
            irc_notifier('Reconnected to an available Wi-Fi network.')
