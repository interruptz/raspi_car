#!/usr/bin/env python

import irc.client
import sandbox

class IRCBot(irc.client.SimpleIRCClient):
    def __init__(self, channels):
        super(IRCBot, self).__init__()
        self.channels = channels
        self.ready = False
    def on_welcome(self, conn, event):
        for x in self.channels:
            conn.join(x) 
        self.ready = True 
    def on_join(self, conn, event):
        #print 'join', event.arguments, event.source, event.target, event.type
        pass
    def on_privmsg(self, conn, event):
        #print 'privmsg', event.arguments, event.source, event.target, event.type
        self.process_command(self, event)
    def on_pubmsg(self, conn, event):
        #print 'pubmsg', event.arguments, event.source, event.target, event.type
        self.process_command(self, event)
    def process_command(self, conn, event):
        msg = event.arguments[0] 
        if len(msg) > 0 and msg[0] == '!':
            msg = msg.split(' ')
            cmd = msg[0].upper()
            param = ' '.join(msg[1:])
            if cmd == '!PY':
                try:
                    r = str(sandbox.eval(param))
                except Exception,e:
                    r = "!!! %s"  % (str(e),)
                self.connection.privmsg(event.target, r.replace('\n', ' ').replace('\r', '')[:256])