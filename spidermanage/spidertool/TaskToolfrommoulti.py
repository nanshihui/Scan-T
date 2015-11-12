#!/usr/bin/python
#coding:utf-8
from spidertool import ThreadToolfrommoulti
from threading import Thread,Lock
import datetime
import time
import Queue
import connectpool
import threading
import multiprocess
import multiprocessing
from  ThreadToolfrommoulti import ThreadTool
class TaskTool:
	def __init__(self,isThread=1):
		self.threadtool=ThreadTool(isThread)
		self.isThread=isThread
#		self.threadtool.add_task(self.task)
		if isThread==1:

			self.lock = Lock() #线程锁
			self.q_request =Queue. Queue() #任务所处理的对象队列
			self.q_finish = Queue.Queue() #任务所处理的对象完成队列

		else:
			self.lock = multiprocessing.Manager().Lock()  
			self.q_request=multiprocess.Manager().Queue()
			self.q_finish=multiprocess.Manager().Queue()

		self.running = 0
	#def __del__(self): #解构时需等待两个队列完成

	#	if self.isThread==1:

	#		self.q_request.join()
		#	self.q_finish.join()
	def set_deal_num(self,num):
		self.threadtool.set_Thread_size(num)
	def set_work_size(self,num):
		self.threadtool.set_Work_size(num)
	###
	#	添加作业的时候，是添加一个数组进去的，避免频繁的添加
	#
	#
	###
	def push(self,req):
		self.q_request.put(req)
	def add_work(self,work):
		temptask=[]
		if self.isThread==1:

			for url in work:
				self.push(url)
				temptask.append(self.getTask)
		else:
			for url in work:
				self.push(url)
				temptask.append(self.getTaskProcess)
		self.threadtool.add_Work(temptask, work)
	def append_work(self,work):
		temptask=[]
		if self.isThread==1:

			for url in work:
				self.push(url)
				temptask.append(self.getTask)
		else:
			for url in work:
				self.push(url)
				temptask.append(self.getTaskProcess)
		self.threadtool.append_Work(temptask, work)		
	def task(self,req,threadname,args):
		print threadname+'执行任务中'+str(datetime.datetime.now())+'         '+args+'    '+req
		
		ans =threadname+'任务结束'+str(datetime.datetime.now()) 
		return ans
	def start_task(self):
		self.threadtool.start()
	def get_finish_work(self):
		if self.has_work_left()>0:

			return self.pop()
		else:
			return 
	def has_work_left(self):
		#return self.threadtool.taskleft()
		return self.q_request.qsize()+self.q_finish.qsize()+self.running
	def pop(self):
		return self.q_finish.get()
	def do_job(self,job,req,threadname,args):
		return job(req,threadname,args)

	def getTaskProcess(self,args):
		while True:
			if self.has_work_left()>0:
				try:
					req = self.q_request.get(block=True,timeout=3)
				except:
					continue
			else:
				threadname=multiprocess.current_process().name
				print threadname+'总任务关闭'
				break
			with self.lock:				#要保证该操作的原子性，进入critical area
				self.running=self.running+1
#			self.lock.acquire()
			threadname=multiprocess.current_process().name

			print '进程'+threadname+'发起请求: '

			ans=self.do_job(self.task,req,threadname,args)
#			ans = self.connectpool.getConnect(req)

# 			self.lock.release()
			self.q_finish.put((req,ans))
#			self.lock.acquire()
			with self.lock:
				self.running-= 1
			threadname=multiprocess.current_process().name

	 		print '进程'+threadname+'完成请求'
#			self.lock.release()

			#self.q_request.task_done()

	def getTask(self,args):
		while True:
			if self.has_work_left()>0:
				try:
					req = self.q_request.get(block=True,timeout=5)
				except:
					continue
			else:
				threadname=threading.currentThread().getName()
				print threadname+'总任务关闭'
				break
			with self.lock:				#要保证该操作的原子性，进入critical area
				self.running=self.running+1
#			self.lock.acquire()
			threadname=threading.currentThread().getName()

			print '线程'+threadname+'发起请求: '

			ans=self.do_job(self.task,req,threadname,args)
#			ans = self.connectpool.getConnect(req)

# 			self.lock.release()
			self.q_finish.put((req,ans))
#			self.lock.acquire()
			with self.lock:
				self.running-= 1
			threadname=threading.currentThread().getName()

			print '线程'+threadname+'完成请求'
		 	self.q_request.task_done()
#			self.lock.release()
if __name__ == "__main__":
	work_manager =  TaskTool(0)#或者work_manager =  WorkManager(10000, 20)
	work_manager.set_deal_num(5)
	#work_manager.set_Work_size(6)
	work_manager.add_work(['a','b','c','d','e','f','g','h','i','j'])
	work_manager.add_work(['k','l','m','n','o','p','q','r','s','t'])

	work_manager.start_task()
#	work_manager.append_work(['k','l','m','n','o','p','q','r','s','t'])

	while work_manager.has_work_left():
		a,b=work_manager.pop()
		print a
	work_manager.append_work(['u','v','w','x','y','z','aa','bb','cc','dd'])
#	work_manager.append_work(['u','v','w','x','y','z','aa','bb','cc','dd'])
	while work_manager.has_work_left():
		a,b=work_manager.pop()
		print a
	while True:
		pass

