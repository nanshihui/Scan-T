#!/usr/bin/python
#coding:utf-8
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os 
def tick():
    print('Tick! The time is: %s' % datetime.now())
class schedulecontrol:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
 

    def addschedule(self,event, day_of_week='0-7', hour='11',minute='57' ,second='0',id=''):
        if id=='':
            id=str(time.strftime("%Y-%m-%d %X", time.localtime()));
        self.scheduler.add_job(event,'cron', day_of_week=day_of_week, hour=hour,minute=minute ,second=second,id=id)    
    def removeschedule(self,id):
        self.scheduler.remove_job(id)
if __name__ == "__main__":           
    temp=schedulecontrol()
    temp.addschedule(tick,'0-7','0-23','0-59','*/5')
    while True:
        pass
       
       
       