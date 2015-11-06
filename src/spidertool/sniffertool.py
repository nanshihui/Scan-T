#!/usr/bin/python
#coding:utf-8

'''
Created on 2015年10月29日

@author: sherwel
'''

import sys
import nmap   
import os
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
class SniffrtTool(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        try:
            self.nm = nmap.PortScanner()                                     # instantiate nmap.PortScanner object
            self.nma = nmap.PortScannerAsync()
            self.params='-A -P0   -Pn  -sC   '
            self.port='  '
        except nmap.PortScannerError:
            print('Nmap not found', sys.exc_info()[0])

        except:
            print('Unexpected error:', sys.exc_info()[0])
    def scan(self,hosts='localhost', arguments='-A -P0   -Pn  -sC   ', callback=''):
        if callback=='':
            
            self.nma.scan(hosts=hosts, arguments=self.params+self.port, callback=self.callback_result)
        else:
            self.nma.scan(hosts=hosts, arguments=self.params+self.port, callback=callback)   
    def set_port(self,port):
        self.port+=' -p '+port
    def callback_result(self,host, scan_result):
        print scan_result
        
        
    def isrunning(self):
        return self.nma.still_scanning()
def callback_result(host, scan_result):
    print '——————'
    print host, scan_result
    tmp=scan_result
    result=''
    result = result + "ip地址:%s 主机名:[%s]  ......  %s\n" %(host,tmp['scan'][host]['hostname'],tmp['scan'][host]['status']['state'])
    try:
        ports = tmp['scan'][host]['tcp'].keys()
        for port in ports:
            info = ''
            portinfo = "%s port : %s  state : %s  product : %s \n" %(info,port,tmp['scan'][host]['tcp'][port]['state'],   tmp['scan'][host]['tcp'][port]['product'])
            result = result + portinfo
    except IOError,e:
        print e
    print result
"""
def callback_resultl(host, scan_result):
    print scan_result
    print scan_result['scan']
    f = open('abc.xml','w+')
    f.write(str(scan_result))
    f.close()
"""


order=' -P0 -sV -sC  -sU  -O -v  -R -sT  '
orderq='-A -P0   -Pn  -sC  -p '


if __name__ == "__main__":   
    temp=SniffrtTool()
    hosts='127.0.0.1'
    temp.scan(hosts)
    while temp.isrunning():
        temp.nma.wait(2)




