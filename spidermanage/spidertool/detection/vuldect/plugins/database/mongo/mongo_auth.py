#!/usr/bin/env python
# encoding: utf-8
from t import T
from pymongo import MongoClient
import requests,urllib2,json,urlparse
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):

        result = {}
        result['result']=False
        r=None
        try:

            r = MongoClient(ip, 27017, connectTimeoutMS=1000, socketTimeoutMS=1000, waitQueueTimeoutMS=1000)


            serverInfo = r.server_info()

            dbList = r.database_names()



            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='MongoClient unauth'
            result['VerifyInfo']['URL'] =ip+':'+port
            result['VerifyInfo']['payload']='None'
            result['VerifyInfo']['result'] ='MongoClient unauth'
            result['VerifyInfo']['level'] = 'hole'

        except Exception,e:
            print e.text
        finally:
            if r is not None:
                r.close()
                del r
            return result
if __name__ == '__main__':
    print P().verify(ip='140.114.108.4',port='80')