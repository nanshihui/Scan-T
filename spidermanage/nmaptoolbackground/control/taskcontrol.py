from spidertool import sniffertask,zmaptool
import schedule
from datetime import datetime
import time
import logging
import random
logging.basicConfig()
nmaptask=None
mainschedule=None
def getObject():
    global nmaptask
    if nmaptask is None:
        nmaptask=sniffertask.snifferTask(1)
        nmaptask.set_deal_num(5)
    return nmaptask
operator = {'1':'80','2':'8080','3':'443','4':'22','5':'23'}  
def tick():
    num=random.randint(1, 1)

    temp=zmaptool.Zmaptool()
    
    temp.do_scan(port=operator.get(str(num)),num='100')
    print('Tick! The time is: %s' % datetime.now())

def taskinit():
    global  nmaptask 
    nmaptask= sniffertask.snifferTask(0)
    nmaptask.set_deal_num(5)
def taskadd(array):
    global  nmaptask 
    if nmaptask is None:
        nmaptask =sniffertask.snifferTask(0)
    nmaptask.add_work(array)
def addschedule(event, day_of_week='0-7', hour='11',minute='57' ,second='0',id=''):
    global mainschedule
    if mainschedule is None:
        mainschedule=schedule.schedulecontrol()
    mainschedule.addschedule(tick,day_of_week,hour,minute,second,id=id)
def scheduleinit():
    global mainschedule
    mainschedule=schedule.schedulecontrol()
    mainschedule.addschedule(tick,'0-7','0-23','*/50','0',id='zmap')

    print 'init schedule'

