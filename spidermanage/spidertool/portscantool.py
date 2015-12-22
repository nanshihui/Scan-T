
#!/usr/bin/python
#coding:utf-8
import time
import re

import os
import SQLTool
import config
import socket
portway = {'sip':'INVITE  world \r\n\r\n','2':'8080','3':'443','4':'22','5':'23'}  
class Portscantool:
    def __init__(self):
        
        socket.setdefaulttimeout(8)
        self.config=config.Config

    def do_scan(self,ip,port,name):
        try:

            self.socketclient=  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketclient.connect((ip,int(port)))

#             message = "GET / HTTP/1.1\r\nHost: oschina.net\r\n\r\n"
            message =portway.get(name,"GET  world \r\n\r\n")
            self.socketclient.sendall(message)
            reply = self.socketclient.recv(4096)
            self.socketclient.close()
            return 'reply',reply
        except Exception, msg:
            print 'Failed to create socket. Error code: ' + str(msg)
            return 'error','error'

   
if __name__ == "__main__":
    temp=Portscantool()
    temp.do_scan('218.104.51.44', '5060')
#     temp.do_scan('218.106.87.35', '110')
    












 
