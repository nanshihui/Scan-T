#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
from TaskTool import TaskTool
from sniffertool import  SniffrtTool
from Job_item import Job_Item 
class snifferTask(TaskTool):
    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        
    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())
        sniffer= SniffrtTool()
        hosts=req.getAddress();
        ports=req.getPort()
        arguments=req.getArguments()
        print (hosts,ports,arguments)
        def callback_resultl(host, scan_result):
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
                print '地址为： ' +req.getAddress()
        ans = sniffer.scanaddress(hosts, ports, callback_resultl, arguments)
        
        while sniffer.isrunning():
            print 'is running : '+threadname
            sniffer.nma.wait(2)
        print threadname+'任务结束'+str(datetime.datetime.now())
        return ans
    
if __name__ == "__main__":   
    links = []
    temp= Job_Item(jobaddress='www.bnuz.edu.cn',jobname='task1')
    temp1= Job_Item(jobaddress='localhost',jobname='task2')
    temp2= Job_Item(jobaddress='www.cctv.com',jobname='task3')
    temp3= Job_Item(jobaddress='www.vip.com',jobname='task4')
    links.append(temp)
    links.append(temp1)
    links.append(temp2)
    links.append(temp3)
    S_produce= snifferTask()#表示创建的是线程
    S_produce.set_deal_num(10)
    S_produce.add_work(links)
    while S_produce.has_work_left():
        
        a,b=S_produce.get_finish_work()



