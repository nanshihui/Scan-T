#!/usr/bin/env python
# coding:utf-8
"""
    Title:Script language recognition
    Description:Automatic identification of PHP, ASP,JSP, ASPX, HTML
    Author:codier
    Blog:http://www.codier.cn
    Date:2015-07-25
"""
import re
import urlparse
from ..miniCurl import Curl
from ..t  import T

#识别脚本语言
def getScript(url):
    curl = Curl()
    app_suffix = []
    signature_buff = ['php','asp.net']
    session_buff = ['aspsessionid-asp','jsessionid-jsp','phpsessid-php','asp.net_sessionid-aspx']
    web_suffix = ['php','asp','aspx','jsp']
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200:
        m = re.search('X-Powered-By: (.*?)[\r|\n]+', head,flags=re.S)
        if m:
            buff = m.group(1).lower()
            for index in signature_buff:
                if index in buff:
                    app_suffix.append(index)
                    
        m = re.search('Set-Cookie: (.*?)=', head,flags=re.S)
        if m:
            buff = m.group(1).lower()
            for index in session_buff:
                if (index[:index.find('-')] in buff) and (index[index.find('-')+1:] not in app_suffix):
                    app_suffix.append(index[index.find('-')+1:])

        m = re.findall(r'href=(?:"|\'|\s)*[/\w]*\.(jsp|php|aspx|asp)',res,re.I)
        if m:
            max_buff = 'asp'
            for index in web_suffix:
                if m.count(index) > m.count(max_buff):
                    max_buff = index
            if max_buff not in app_suffix:
                app_suffix.append(max_buff)


        if 'asp' in app_suffix or 'aspx' in app_suffix :
            if 'asp.net' in app_suffix:app_suffix.remove('asp.net')
        if len(app_suffix) == 0:app_suffix.append('html')
    del curl
    return app_suffix


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'

        result = {}
        result['result']=False

        app_suffix = getScript(arg)
        if len(app_suffix) != 0:
            output(arg+' the language they use is '+ str(app_suffix),result,'note')



        return result


def output(url,result,label):
    info = url + '  Script language recognition'
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='Script language recognition'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='language detect'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':

    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_2cd6e35ac47714c13206836991b19fa6.py
#/root/github/poccreate/codesrc/exp-1176.py