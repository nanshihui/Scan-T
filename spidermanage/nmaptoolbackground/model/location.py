#!/usr/bin/python
#coding:utf-8
try:
    from spidertool.detection.httpdect.webdection import getgeoipinfo
except:
    pass
class Location(object):
    def __init__(self,ip=None):

        data={}
        data['ip']=[ip]
        from spidertool import redistool
        redisresult = redistool.get(ip)
        if redisresult:

            self.data = redisresult
        else:
            keyword=''
            try:
                keyword = getgeoipinfo.getGeoipinfo(data)
            except:
                pass
            redistool.set(ip, keyword)

            self.data=keyword


    def getData(self):
        return self.data