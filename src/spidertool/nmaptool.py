#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
Created on 2015年10月29日

@author: dell
'''

import nmap
import re

import sys
from multiprocessing import Pool
from functools import partial

def nmScan(host,portrange,whitelist):
    p = re.compile("^(\d*)\-(\d*)$")
    # if type(hostlist) != list:
    #     help()
    portmatch = re.match(p,portrange)
    if not portmatch:
        help()
    if host == '121.42.32.172':
        whitelist = [25,]
    result = ''
    nm = nmap.PortScanner()
    tmp = nm.scan(host,portrange)
    result = result + "<h2>ip地址:%s 主机名:[%s]  ......  %s</h2><hr>" %(host,tmp['scan'][host]['hostname'],tmp['scan'][host]['status']['state'])
    try:
        ports = tmp['scan'][host]['tcp'].keys()
        for port in ports:
            info = ''
            if port not in whitelist:
                info = '<strong><font color=red>Alert:非预期端口</font><strong>  '
            else:
                info = '<strong><font color=green>Info:正常开放端口</font><strong>  '
        portinfo = "%s <strong>port</strong> : %s   <strong>state</strong> : %s   <strong>product<strong/> : %s <br>" %(info,port,tmp['scan'][host]['tcp'][port]['state'],                                                                       tmp['scan'][host]['tcp'][port]['product'])
        result = result + portinfo
    except KeyError,e:
        if whitelist:
            whitestr = ','.join(whitelist)
            result = result + "未扫到开放端口!请检查%s端口对应的服务状态" %whitestr                
        else:
            result = result + "扫描结果正常，无暴漏端口"           
    return result
def help():
    print "Usage: nmScan(['127.0.0.1',],'0-65535')"
    return None
if __name__ == "__main__":   
    hostlist = ['10.10.10.1','10.10.10.2']
    pool = Pool(5)
    nmargu = partial(nmScan,portrange='0-65535',whitelist=[])
    results = pool.map(nmargu,hostlist)