#!/usr/bin/python
#coding:utf-8
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
def tick():
    print('Tick! The time is: %s' % datetime.now())
class schedulecontrol:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.oncescheduler=BlockingScheduler()
        self.scheduler.start()
    def start(self):
        self.oncescheduler.start()
    def addschedule(self,event=None, day_of_week='0-7', hour='11',minute='57' ,second='0',id='',type='cron',run_date='',args=None):
        if id=='':
            id=str(time.strftime("%Y-%m-%d %X", time.localtime()));
        if type=='date':
            if run_date=='':

                self.oncescheduler.add_job(event, args=args)


            else:

                self.oncescheduler.add_job(event, 'date', run_date=run_date, args=args)
        elif type=='back':
            self.oncescheduler.add_job(event,type, day_of_week=day_of_week, hour=hour,minute=minute ,second=second,id=id)
        else:

            self.scheduler.add_job(event, type, day_of_week=day_of_week, hour=hour, minute=minute, second=second, id=id)
    def removeschedule(self,id):
        self.scheduler.remove_job(id)
if __name__ == "__main__":
    pass
#     temp=schedulecontrol()
#     temp.addschedule(event=tick,type='date')
#
#     temp.start()

#     temp.addschedule(event=tick,type='date')
#     while True:
#         pass


