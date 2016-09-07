#!/usr/bin/python
#coding:utf-8

import schedule


import logging


logging.basicConfig()#日志基础配置
mainschedule=None
#定时任务添加函数
def addschedule(event, day_of_week='0-7', hour='11',minute='57' ,second='0',id=''):
    global mainschedule
    if mainschedule is None:
        mainschedule=schedule.schedulecontrol()
    mainschedule.addschedule(event,day_of_week,hour,minute,second,id=id)
#定时任务初始化函数
def scheduleinit():
    from spidertool import scapytool
    import taskitem
#     scapyitem=scapytask.ScapyTask()#被动嗅探
    global mainschedule
    mainschedule=schedule.schedulecontrol()
    # mainschedule.addschedule(taskitem.listiptask,'0-7','*/21','13','0',id='listiptask')#自定义扫描段任务器
    mainschedule.addschedule(taskitem.tick,'0-7','0-23','*/10','0',id='nmap')#nmap定时任务器
#     mainschedule.addschedule(taskitem.zmaptask,'0-7','0-23','*/8','0',id='zmap')#zmap定时任务器
    # mainschedule.addschedule(event=taskitem.text,type='date')#一次性任务器
    # mainschedule.addschedule(event=tempw.dowork,type='date')
    mainschedule.start()
    print 'init schedule'

