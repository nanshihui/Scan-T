# !/usr/bin/env python
# -*- coding:utf-8 -*-

class IPTool():
    def __init__(self):
        pass

#字符串IP转化为数字的IP

    def ip2num(self,ip):
        lp = [int(x) for x in ip.split('.')]
        return lp[0] << 24 | lp[1] << 16 | lp[2] << 8 |lp[3]

#数字的IP转化为字符串

    def num2ip(self,num):
        ip = ['','','','']
        ip[3] = (num & 0xff)
        ip[2] = (num & 0xff00) >> 8
        ip[1] = (num & 0xff0000) >> 16
        ip[0] = (num & 0xff000000) >> 24
        return '%s.%s.%s.%s' % (ip[0],ip[1],ip[2],ip[3])
#计算输入的ip范围

    def iprange(self,ip1,ip2):
        num1 = self.ip2num(ip1)
        num2 = self.ip2num(ip2)
        tmp = num2 - num1
        if tmp < 0:
            return None
        else:
            return num1,num2,tmp

    def getIplist(self,startip,endip):
        ip_list = []
        res = ()
        res = self.iprange(startip,endip)
        if res < 0:
            print 'endip must be bigger than startone'
            return ip_list
        else:
            for x in xrange(int(res[2])+1):
                startipnum = self.ip2num(startip)
                startipnum = startipnum + x
                ip_list.append(self.num2ip(startipnum))
            return ip_list
if __name__ == '__main__':
    a=IPTool()
    list=a.getIplist('219.235.6.52','219.235.6.59')
    print list