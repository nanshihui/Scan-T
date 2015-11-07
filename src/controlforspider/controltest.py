'''
Created on 2015年11月7日

@author: dell
'''
#!/usr/bin/python
#coding:utf-8
from spidertool import sniffertask
from spidertool import dealTask
from spidertool import SQLTool
import datetime
from spidertool import Job_item
if __name__ == '__main__':
    links = []
    temp= Job_item.Job_Item(jobaddress='http://www.bunz.edu.cn',jobname='task1')
    temp1= Job_item.Job_Item(jobaddress='http://www.hao123.com',jobname='task2')
    temp2= Job_item.Job_Item(jobaddress='http://www.cctv.com',jobname='task3')
    temp3= Job_item.Job_Item(jobaddress='http://www.vip.com',jobname='task4')
    links.append(temp)
    links.append(temp1)
    links.append(temp2)
    links.append(temp3)
    S_produce= sniffertask.snifferTask()#表示创建的是线程
    S_produce.set_deal_num(10)
    S_produce.add_work(links)

    #S_produce.start_task()

    searchResultSQL=SQLTool.DBmanager()
    searchResultSQL.connectdb()
    F_consume=dealTask.dealTask(0)#参数0表示创建的是进程
    F_consume.set_deal_num(10)
    
    while S_produce.has_work_left():
        v,b=S_produce.get_finish_work()

        searchResultSQL.inserttableinfo_byparams('webdata', ["address","content","meettime"], [(v,b,str(datetime.datetime.now()))])        
        F_consume.add_work(b)
    while True:
        pass