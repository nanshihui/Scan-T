#!/usr/bin/python
#coding:utf-8

'''
Created on 2015年10月29日

@author: sherwel
'''

import sys
import nmap   
import os
from numpy.numarray.numerictypes import IsType
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
            self.params='-A -P0   -Pn  -sC  -R -v  -O '

        except nmap.PortScannerError:
            print('Nmap not found', sys.exc_info()[0])

        except:
            print('Unexpected error:', sys.exc_info()[0])
    def scan(self,hosts='localhost', port='', callback='',arguments=''):
        orders=''
        if port!='':
            orders+='   -p '+port
        if callback=='':
            print type(self.callback_result);
            self.nma.scan(hosts=hosts, arguments=self.params+arguments+orders, callback=self.callback_result)
        else:
            self.nma.scan(hosts=hosts, arguments=self.params+arguments+orders, callback=callback)   

    def callback_result(self,host, scan_result):
        print 'test'
        print scan_result
        
    def scanaddress(self,hosts=[], ports=[], call_back='',arguments=''):
        for i in range(len(hosts)):
            if len(ports)<=i:
                self.scan(hosts=hosts[i], callback=call_back,arguments=arguments)
            else:
                    
                self.scan(hosts=hosts[i], port=ports[i], callback=call_back,arguments=arguments)
            
    def isrunning(self):
        return self.nma.still_scanning()
def callback_resultl(host, scan_result):
    print scan_result
    print '——————'
    tmp=scan_result
    result=''

    try:
        result =  u"ip地址:%s 主机名:%s  ......  %s\n" %(host,tmp['scan'][host]['hostname'],tmp['scan'][host]['status']['state'])
        if 'osclass' in tmp['scan'][host].keys():
            result +=u"系统信息 ： %s %s %s   准确度:%s  \n" % (str(tmp['scan'][host]['osclass']['vendor']),str(tmp['scan'][host]['osclass']['osfamily']),str(tmp['scan'][host]['osclass']['osgen']),str(tmp['scan'][host]['osclass']['accuracy']))
        if 'tcp' in  tmp['scan'][host].keys():
            ports = tmp['scan'][host]['tcp'].keys()
            for port in ports:

                portinfo = " port : %s  name:%s  state : %s  product : %s version :%s  script:%s \n" %(port,tmp['scan'][host]['tcp'][port]['name'],tmp['scan'][host]['tcp'][port]['state'],   tmp['scan'][host]['tcp'][port]['product'],tmp['scan'][host]['tcp'][port]['version'],tmp['scan'][host]['tcp'][port]['script'])
                result = result + portinfo
        elif 'udp' in  tmp['scan'][host].keys():
            ports = tmp['scan'][host]['udp'].keys()
            for port in ports:
                portinfo = " port : %s  name:%s  state : %s  product : %s  version :%s  script:%s \n" %(port,tmp['scan'][host]['udp'][port]['name'],tmp['scan'][host]['udp'][port]['state'],   tmp['scan'][host]['udp'][port]['product'],tmp['scan'][host]['udp'][port]['version'],tmp['scan'][host]['udp'][port]['script'])
                result = result + portinfo
    except Exception,e:
        print e
    except IOError,e:
        print '错误IOError'+str(e)
    except KeyError,e:
        print '不存在该信息'+str(e)
    finally:
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
    hosts=['localhost','www.bnuz.edu.cn','www.baidu.com']
    temp.scanaddress(hosts,arguments='',call_back=callback_resultl)
    while temp.isrunning():
        temp.nma.wait(2)




