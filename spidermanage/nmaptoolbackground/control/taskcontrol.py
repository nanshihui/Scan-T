from spidertool import sniffertask,zmaptool
import schedule
from datetime import datetime
import time
import logging
logging.basicConfig()
nmaptask=None
mainschedule=None
def tick():

    temp=zmaptool.Zmaptool()
    temp.do_scan()
    print('Tick! The time is: %s' % datetime.now())
def taskinit():
    nmaptask =sniffertask.snifferTask(1)
    nmaptask.set_deal_num(5)
def taskadd(array):
    if nmaptask is None:
        nmaptask =sniffertask.snifferTask(1)
    nmaptask.add_work(array)
def addschedule(event, day_of_week='0-7', hour='11',minute='57' ,second='0',id=''):
    if mainschedule is None:
        mainschedule=schedule.schedulecontrol()
    mainschedule.addschedule(tick,day_of_week,hour,minute,second,id=id)
def scheduleinit():
    mainschedule=schedule.schedulecontrol()
    mainschedule.addschedule(tick,'0-7','0-23','0','0',id='zmap')

    print 'init schedule'
