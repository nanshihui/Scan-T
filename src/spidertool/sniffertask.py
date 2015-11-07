#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
from TaskTool import TaskTool
from sniffertool import  SniffrtTool
class snifferTask(TaskTool):
    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        self.sniffer=SniffrtTool()
    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())
        hosts=req.getAddress();
        ports=req.getPort()
        arguments=req.getArguments()
        ans = self.sniffer.scanaddress(hosts, ports, callback_resultl, arguments)
        
        print threadname+'任务结束'+str(datetime.datetime.now())
        return ans

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
        print '错误KeyError'+str(e)
    finally:
            print result


