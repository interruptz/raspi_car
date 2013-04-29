#!/usr/bin/env python

IP = '192.168.0.37' #raw_input('IP   : ')
PORT = 5000 #int(raw_input('Port : '))

HOST = (IP, PORT)

from Tkinter import *
import socket

root = Tk()
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(HOST)

def keypress(event):
    sck.send(event.char)

msg = 'w=Up, s=Down, a=Left, d=Right\nq=Stop'
label = Label(root, text=msg, width=len(msg), bg='yellow')
label.pack()

root.bind_all('<Key>', keypress)
root.title('Remote Controller for Minicar')
root.mainloop()
