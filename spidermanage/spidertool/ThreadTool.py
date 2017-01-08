#!/usr/bin/python
#coding:utf-8




import threading
from threading import Thread,Lock


from Queue import Queue
import time
from threading import stack_size
import datetime
import multiprocessing


once=None


stack_size(32768*16)
class ThreadTool:
	def __init__(self,isThread=1,needfinishqueue=0,deamon=False):
		self.isThread=isThread
		self.idletask={}
		self.Threads=[]
		self.alivenum=0
		self.needfinishqueue=needfinishqueue
		self.running = 0
		self.threads_num = 10
		self.deamon=deamon
		self.job=None
		self.default_object=None
		if self.isThread==1:
			# self.lock = Lock() #线程锁
			self.lock=threading.Lock()
			self.q_request = Queue() #任务队列
			if needfinishqueue>0:
				self.q_finish = Queue() #完成队列
		elif self.isThread==0 :
			self.lock = multiprocessing.Lock()  
			self.q_request=multiprocessing.Queue()
			if self.needfinishqueue>0:
				self.q_finish=multiprocessing.Queue()
		else:

			from gevent.queue import JoinableQueue as geventqueue
			from gevent.lock import Semaphore

			from gevent import monkey
			global once
			if once is None:
				monkey.patch_all()
				once=1
			self.lock = Semaphore()
			self.q_request = geventqueue()
			if self.needfinishqueue > 0:
				self.q_finish = geventqueue()

	def __del__(self): #解构时需等待两个队列完成
		time.sleep(0.5)
		if self.isThread==1 or self.isThread==2:

			self.q_request.join()
			if self.needfinishqueue>0:
				self.q_finish.join()


	def getqueue_size(self):
		return self.q_request.qsize()
	def set_Thread_size(self,threads_num=10):
		self.threads_num = threads_num
	def init_add(self,add_init_object):
		self.default_object=add_init_object
	def add_task(self,job):
		self.job=job
#获取当前剩余的任务，用于集群操做
	def get_work(self):
		tmparray=[]
		if self.q_request.qsize()>0:
			try:
				req = self.q_request.get(block=True,timeout=4)
				tmparray.append(req)
				return tmparray
			except:
				return tmparray
		else:
			return tmparray
	def start(self):
		sizenumber=min(self.threads_num,self.q_request.qsize())
		if self.isThread==1:
			for i in range(sizenumber):
				t = Thread(target=self.getTask)
				print '线程'+str(i+1)+'  正在启动'
				t.setDaemon(self.deamon)
				t.start()
				self.Threads.append(t)
				with self.lock:	
					self.alivenum+=1
		elif self.isThread==0:
			for i in range(sizenumber):
				t = multiprocessing.Process(target=self.getTaskProcess)
				print '进程'+str(i+1)+'  正在启动'
				t.Daemon=self.deamon
				t.start()	
				self.Threads.append(t)
				with self.lock:	
					self.alivenum+=1
		else:
			import gevent
			for i in range(sizenumber):
				t = gevent.spawn(self.getgeventTask)
				print '协程' + str(i + 1) + '  正在启动'
				self.Threads.append(t)
				with self.lock:
					self.alivenum += 1
	def get_running_size(self):
		return self.running
	def taskleft(self):
		if self.needfinishqueue>0:
			return self.q_request.qsize()+self.q_finish.qsize()+self.running
		else:
			return self.q_request.qsize()+self.running
	def push(self,req):
		sizenum=len(req)
		for urls in req:
			self.q_request.put(urls)

		threadnownum=0
		threaddie=[]
		dienum=0
		if self.isThread==1:
			tempnumb=0
			with self.lock:
				tempnumb=self.alivenum
			if tempnumb<self.threads_num:
					
				for item in self.Threads:

					if item.isAlive():


						threadnownum=threadnownum+1


				with self.lock:	
					print str(threadnownum)+'活着的线程数'
					self.Threads = filter(lambda x:x.isAlive() !=False,self.Threads)
				print str(len(self.Threads))+'清理后活着的线程数'
			else:
				threadnownum=self.threads_num
		elif self.isThread==0:
			tempnumb=0
			time.sleep(1)
			with self.lock:
				if len(self.Threads) == 0:
					threadnownum = 0
				else:
					self.Threads = filter(lambda x: x.is_alive() != False, self.Threads)
					tempnumb= len(self.Threads)
			if tempnumb<self.threads_num:
				threadnownum=tempnumb

			else:
				threadnownum=self.threads_num
			
		sizenumber=min(self.threads_num-threadnownum,sizenum)
		if self.isThread==1:
			for i in range(sizenumber):
				t=Thread(target=self.getTask)
				t.setDaemon(self.deamon)
				with self.lock:
					self.alivenum+=1
				t.start()
				self.Threads.append(t)


		elif self.isThread==0:
			for i in range(sizenumber):
				t=multiprocessing.Process(target=self.getTaskProcess)
				t.daemon=self.deamon
				with self.lock:
					self.alivenum+=1
				t.start()
				self.Threads.append(t)



		else:
			import gevent
			for i in range(self.threads_num):
				if self.alivenum <self.threads_num:
					t = gevent.spawn(self.getgeventTask)
					print '协程' + str(self.alivenum) + '  正在启动'
					self.Threads.append(t)
					with self.lock:
						self.alivenum += 1
				else:
					break

			self.q_request.join()

	def pop(self):
		return self.q_finish.get()
	def do_job(self,job,req,threadname):
		return job(req,threadname)

	def getTaskProcess(self):
		req=None
		while True:
			if self.taskleft()>0:
				try:
					req = self.q_request.get(block=True,timeout=1000)
				except:
					continue
			else:
				try:
					req = self.q_request.get(block=True,timeout=60*60)
					threadname = multiprocessing.current_process().name
				except Exception,e:
					with self.lock:
						self.alivenum-=1
					print threadname+'关闭'
					break


			with self.lock:

				self.running=self.running+1

			threadname=multiprocessing.current_process().name

			print '进程'+threadname+'发起请求: '

			ans=self.do_job(self.job,req,threadname)

			if self.needfinishqueue>0:
				self.q_finish.put((req,ans))
			with self.lock:
				self.running= self.running-1
			threadname=multiprocessing.current_process().name

			print '进程'+threadname+'完成请求'



	def getTask(self):
		while True:
			if self.taskleft()>0:
				try:
					req = self.q_request.get(block=True,timeout=1000)
				except:
					continue
			else:
				try:
					req = self.q_request.get(block=True,timeout=60*60)
					threadname=threading.currentThread().getName()
				except:

					with self.lock:
						self.alivenum-=1
					print threadname+'关闭'
					break


			with self.lock:				#要保证该操作的原子性，进入critical area
				self.running=self.running+1


			threadname=threading.currentThread().getName()

			print '线程'+threadname+'发起请求: '

			ans=self.do_job(self.job,req,threadname)

			if self.needfinishqueue>0:
				self.q_finish.put((req,ans))
			with self.lock:
				self.running-= 1
			threadname=threading.currentThread().getName()

			print '线程'+threadname+'完成请求'
			self.q_request.task_done()
	def getgeventTask(self):
		import gevent
		while True:
			if self.taskleft()>0:
				try:
					req = self.q_request.get(block=True,timeout=10000)
				except:
					continue
			else:
				threadname=threading.currentThread().getName()
				with self.lock:
					self.alivenum-=1
				print threadname+'关闭'
				break

			with self.lock:				#要保证该操作的原子性，进入critical area
				self.running=self.running+1


			threadname=gevent.getcurrent()

			print threadname,'协程发起请求: '

			ans=self.do_job(self.job,req,threadname)

			if self.needfinishqueue>0:
				self.q_finish.put((req,ans))
			with self.lock:
				self.running-= 1
			threadname = gevent.getcurrent()

			print threadname, '协程发起请求: '
			self.q_request.task_done()

def taskitem(req,threadname):
	print threadname,req,'执行任务中'

	time.sleep(3)
	return threadname,'任务结束'+str(datetime.datetime.now())

if __name__ == "__main__":
	t=ThreadTool()
	t.push()
