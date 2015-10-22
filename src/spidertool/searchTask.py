#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
class searchTask:
	def __init__(self):
		self.threadtool=ThreadTool()
		self.threadtool.add_task(self.task)
	def set_deal_num(self,num):
		self.threadtool.set_Thread_size(num)
	def add_work(self,work):
		for url in work:
			self.threadtool.push(url)
	def task(self,threadname):
		print threadname+'执行任务中'
		print datetime.datetime.now()
		return threadname+'任务结束'+str(datetime.datetime.now())
	def start_task(self):
		self.threadtool.start()
	def get_finish_work(self):
		if self.threadtool.taskleft()>0:

			return self.threadtool.pop()
		else:
			return 
	def has_work_left(self):
		return self.threadtool.taskleft()
if __name__ == "__main__":
	links = [ 'http://www.bunz.edu.com','http://www.baidu.com','http://www.hao123.cx','http://www.cctv.cx','http://www.vip.cx']
	f = searchTask()
	f.set_deal_num(10)
	f.add_work(links)

	f.start_task()
	while f.has_work_left():
		v,b=f.get_finish_work()
		print v
	while True:
		pass




