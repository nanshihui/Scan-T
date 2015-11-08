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
        self.sniffer= SniffrtTool()
    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())

        hosts=req.getAddress();
        ports=req.getPort()
        arguments=req.getArguments()
        print (hosts,ports,arguments)

        ans = self.sniffer.scanaddress(hosts, ports, arguments)

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



