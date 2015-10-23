#!/usr/bin/python
#coding:utf-8
import urllib2
import threading
from threading import Thread,Lock
from Queue import Queue
import time
import connectpool
from threading import stack_size
stack_size(32768*16)
class Threadtool:
	def __init__(self,threads_num=10):

		self.lock = Lock() #线程锁
		self.q_request = Queue() #任务队列
		self.q_finish = Queue() #完成队列
		if threads_num>10:
			self.threads_num=10
		else:
			self.threads_num = threads_num

		self.running = 0
		self.connectpool=connectpool.ConnectPool()
	def __del__(self): #解构时需等待两个队列完成
		time.sleep(0.5)
		self.q_request.join()
		self.q_finish.join()


	def start(self):
		for i in range(self.threads_num):
			t = Thread(target=self.getTask)
			print '线程'+str(i)+'  正在启动'
			t.setDaemon(True)
			t.start()
	def taskleft(self):
		return self.q_request.qsize()+self.q_finish.qsize()+self.running

	def push(self,req):
		self.q_request.put(req)

	def pop(self):
		return self.q_finish.get()

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
			threadname=threading.currentThread().getName()

			print '进程'+threadname+'发起请求: '+req


			ans = self.connectpool.getConnect(req)

# 			self.lock.release()
			self.q_finish.put((req,ans))
#			self.lock.acquire()
			with self.lock:
				self.running-= 1
			threadname=threading.currentThread().getName()

	 		print '进程'+threadname+'完成请求'
#			self.lock.release()

			self.q_request.task_done()



if __name__ == "__main__":
	links = [ 'http://www.bunz.edu.com','http://www.baidu.com','http://www.hao123.cx','http://www.cctv.cx','http://www.vip.cx']
	f = Threadtool(threads_num=5)
	for url in links:
		f.push(url)
	f.start()
	while f.taskleft():
		url,content = f.pop()
		print url