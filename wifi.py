#!/usr/bin/env python 

import hw.net as n
import hw.light as l
import time
import os

def start(t, b):
	n.wifi_on()
	n.wifi_connect()
	while not b.ready:
		time.sleep(0.1)
	b.connection.privmsg(t, 'Connected to an available Wi-Fi network. All systems go!')
	while True:
			time.sleep(60 * 3)
			if not n.net_available():
				n.wifi_off()
				n.wifi_on()
				n.wifi_connect()
				b.connection.privmsg(t, 'Reconnected to an available Wi-Fi network.')