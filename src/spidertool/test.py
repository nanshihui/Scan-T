#!/usr/bin/python
import Queue
def aa():
	print 'already in port'
class bb:
	def __init__(self):
		self.yy=0
		self.qq=Queue.Queue()
		self.qq.put(self.aa)
		self.yy=1
		print 'alread user port'
	def aa(self):
		return self.yy
	def cc(self):
		u=self.qq.get()
		print u()

def asd():
	return 1,2
a=bb()
a.cc()