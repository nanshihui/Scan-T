#!/usr/bin/python
#coding:utf-8
import urllib2
import threading
from threading import Thread,Lock
from Queue import Queue
import time
import connectpool
from threading import stack_size
import datetime
import multiprocessing
stack_size(32768*16)
class ThreadTool:
	def __init__(self,isThread=1):
		self.isThread=isThread
		self.idletask={}
		self.Threads=[]
		if self.isThread==1:
			self.lock = Lock() #线程锁

			self.q_request = Queue() #任务队列
			self.q_finish = Queue() #完成队列
		else :
			self.lock = multiprocessing.Lock()  
			self.q_request=multiprocessing.Queue()
			self.q_finish=multiprocessing.Queue()
		self.running = 0

	def __del__(self): #解构时需等待两个队列完成
		time.sleep(0.5)
		if self.isThread==1:

			self.q_request.join()
			self.q_finish.join()
	def set_Thread_size(self,threads_num=10):
		self.threads_num = threads_num
	def init_add(self,add_init_object):
		self.default_object=add_init_object
	def add_task(self,job):
		self.job=job
	def start(self):
		sizenumber=min(self.threads_num,self.q_request.qsize())
		if self.isThread==1:
			for i in range(sizenumber):
				t = Thread(target=self.getTask)
				print '线程'+str(i+1)+'  正在启动'
				t.setDaemon(True)
				t.start()
				self.Threads.append(t)
		else:
			for i in range(sizenumber):
				t = multiprocessing.Process(target=self.getTaskProcess)
				print '进程'+str(i+1)+'  正在启动'
				t.Daemon=True
				t.start()	
				self.Threads.append(t)
	def taskleft(self):
		return self.q_request.qsize()+self.q_finish.qsize()+self.running

	def push(self,req):
		sizenum=len(req)
		for urls in req:
			self.q_request.put(urls)

		threadnownum=0
		threaddie=[]
		dienum=0
		if self.isThread==1:
			for item in self.Threads:

				if item.isAlive():


					threadnownum=threadnownum+1


			with self.lock:	
				print str(threadnownum)+'活着的线程数'
				self.Threads = filter(lambda x:x.isAlive() !=False,self.Threads)
		else:
			for item in self.Threads:

				if item.is_alive():

					threadnownum=threadnownum+1	


			with self.lock:	
				print str(threadnownum)+'活着的进程数'
				self.Threads = filter(lambda x:x.is_alive()!=False,self.Threads)
		print str(len(self.Threads))+'清理后活着的进程数'


			
		sizenumber=min(self.threads_num-threadnownum,sizenum)
		if self.isThread==1:
			for i in range(sizenumber):
				t=Thread(target=self.getTask)
				t.Daemon=True
				t.start()
				self.Threads.append(t)

		else:
			for i in range(sizenumber):
				t=multiprocessing.Process(target=self.getTaskProcess)
				t.Daemon=True
				t.start()
				self.Threads.append(t)

	def pop(self):
		return self.q_finish.get()
	def do_job(self,job,req,threadname):
		return job(req,threadname)

	def getTaskProcess(self):
		while True:
			if self.taskleft()>0:
				try:
					req = self.q_request.get(block=True,timeout=5)
				except:
					continue
			else:
				threadname=multiprocessing.current_process().name
				print threadname+'关闭'
				break
			with self.lock:				#要保证该操作的原子性，进入critical area
				self.running=self.running+1
#			self.lock.acquire()
			threadname=multiprocessing.current_process().name

			print '进程'+threadname+'发起请求: '

			ans=self.do_job(self.job,req,threadname)
#			ans = self.connectpool.getConnect(req)

# 			self.lock.release()
			self.q_finish.put((req,ans))
#			self.lock.acquire()
			with self.lock:
				self.running-= 1
			threadname=multiprocessing.current_process().name

	 		print '进程'+threadname+'完成请求'
#			self.lock.release()

			#self.q_request.task_done()

	def getTask(self):
		while True:
			if self.taskleft()>0:
				try:
					req = self.q_request.get(block=True,timeout=5)
				except:
					continue
			else:
				threadname=threading.currentThread().getName()
				print threadname+'关闭'
				break
			with self.lock:				#要保证该操作的原子性，进入critical area
				self.running=self.running+1
#			self.lock.acquire()
			self.q_request.task_done()
			threadname=threading.currentThread().getName()

			print '线程'+threadname+'发起请求: '

			ans=self.do_job(self.job,req,threadname)
#			ans = self.connectpool.getConnect(req)

# 			self.lock.release()
			self.q_finish.put((req,ans))
#			self.lock.acquire()
			with self.lock:
				self.running-= 1
			threadname=threading.currentThread().getName()

	 		print '线程'+threadname+'完成请求'
#			self.lock.release()

			

def taskitem(req,threadname):
	print threadname+'执行任务中'
	print datetime.datetime.now()
	return threadname+'任务结束'+str(datetime.datetime.now())


if __name__ == "__main__":
	links = [ 'http://www.bunz.edu.com','http://www.baidu.com','http://www.hao123.cx','http://www.cctv.cx','http://www.vip.cx']
	f = ThreadTool(0)
	f.set_Thread_size(10)
	for url in links:
		f.push(url)
	f.add_task(taskitem)
	f.start()
	timea=1
	while f.taskleft():
		url,content = f.pop()
		print url
	while True:
		pass

