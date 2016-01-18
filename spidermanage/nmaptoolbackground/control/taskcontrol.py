from spidertool import sniffertask
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
def getavailwork():
    global nmaptask
    if nmaptask is None:
        nmaptask=sniffertask.snifferTask(1)
        nmaptask.set_deal_num(5)
        return ''
    else:
        nmaptask.get_work()

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
    from spidertool import scapytool 
    import taskitem
#    scapytool.initsniffer()
    global mainschedule
    mainschedule=schedule.schedulecontrol()

    mainschedule.addschedule(taskitem.tick,'0-7','1-19','*/10','0',id='nmap')   
    mainschedule.addschedule(taskitem.ticknormal,'0-7','20-23','*/10','0',id='zmap')   
    print 'init schedule'

