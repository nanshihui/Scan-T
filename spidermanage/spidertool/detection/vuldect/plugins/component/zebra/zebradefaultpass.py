#!/usr/bin/env python
# encoding: utf-8
from t import T
import os
import platform
import subprocess
import signal
import time
import requests,urllib2,json,urlparse

import pexpect

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):

        result = {}
        result['result']=False
        cmd=None
        passwd='zebra'
        i=0
        cmd = pexpect.spawn('telnet %s %s' %(ip,port) )
        try:

            i = cmd.expect(['Password:','Connection refused'], timeout=2)
            if i==1:
                return result
            cmd.sendline(passwd)

            i = cmd.expect(['Incorrect','>'], timeout=2)
            if i == 0:
                return result




            result['result'] = True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type'] = 'weak  pass'
            result['VerifyInfo']['URL'] = ip + ':' + port
            result['VerifyInfo']['payload'] = passwd
            result['VerifyInfo']['level'] = 'hole'
            result['VerifyInfo']['result'] = 'pass is  %s'% passwd

        except pexpect.EOF:
            pass
        except pexpect.TIMEOUT:
            pass
        finally:
            if cmd is not None:
                cmd.close()
            return result
if __name__ == '__main__':
    print P().verify(ip='222.177.55.119',port='2601')
