#!/usr/bin/env python 

from ircbot import IRCBot 
from remote import RemoteController
import wifi

import os
import threading
import time 
import sys 
# Configuration
config = {
            'remote': {
                'port': 5000
            },
            'irc': {
                'host': ('irc.snoonet.org', 6667),
                'nickname': 'jypcar',
                'channels': ['#lizp']
            }

        }

is_daemon = False
# Process options
for x in sys.argv:
    if x[0] == '-':
        if x[1] == 'd':
            is_daemon = True
        else:
            print """[+] Minicar Operating Program by jyp
            -d: Daemonize this app.
            """
if __name__ == '__main__':
    if is_daemon:
        pid = os.fork() # Demonize itself
    else: 
        pid = 0
    if pid == 0:
        # Initialize
        b = IRCBot(config['irc']['channels'])
        def __init():
            b.connect(config['irc']['host'][0], config['irc']['host'][1], config['irc']['nickname'])
            return b
        def __notifier(m):
            b.connection.privmsg(config['irc']['channels'][0], m) 
        # Threads
        threads = []

        # Add services
        threads.append(threading.Thread(target=wifi.start, args=(__init,__notifier)))
        threads.append(threading.Thread(target=RemoteController.mainloop, args=(config['remote']['port'],)))
        threads.append(threading.Thread(target=b.start))
        # launch services
        map(lambda x: x.start(), threads)
        # wait
        if not is_daemon:
            try:    
                while True:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print 'Program Terminated.'
                os.kill(os.getpid(), 9)
        else:
            threads[0].join()
