#!/usr/bin/env python

import socket
import time
import datetime

import hw.block as bb
from car import Car

class RemoteController(object):
    @classmethod
    def mainloop(self, port):
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sck.bind(('0.0.0.0', port))
        sck.listen(1)
        sck.setblocking(0)
        dt = datetime.datetime.now()
        idle = 0
        while True:
            try:
                client, addr = sck.accept()
            except socket.error:
                time.sleep(0.1)
                continue
            print addr
            while True:
                try:
                    t = client.recv(1)
                    if len(t) == 1: char = ord(t)
                    elif len(t) == 0: 
                        break
                except socket.error:
                    char = -1
                if char != -1:
                    if char == ord('d'): Car.right()
                    elif char == ord('a'): Car.left()
                    elif char == ord('w'):
                        if not bb.is_blocked(): 
                            Car.up()
                        else:
                            Car.stop()
                    elif char == ord('s'): Car.down()
                    dt = datetime.datetime.now()
                    idle = 0
                elif idle >= 2:
                    if Car.moving: 
                        Car.stop() 
                    else:
                        time.sleep(0.1)
                else: 
                    idle += 1
                    time.sleep(0.1)