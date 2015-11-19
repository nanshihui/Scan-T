#!/usr/bin/python
import Queue
import time
import re
def aa():
	print 'already in port'
class bb:
	def __init__(self):
		self.yy=0
		self.qq=Queue.Queue()
		self.qq.put((self.aa,1))
		self.yy=1
		print 'alread user port'
	def aa(self):
		return self.yy
	def cc(self):
		u,k=self.qq.get()
		print u()
		print k
def asd():
	return 1,2
dict = {'a' : ("apple",), 'bo' : {"b" : "banana", "o" : "orange"}, 'g' : ["grape","grapefruit"]}
y=dict.keys()
tmp= str(time.strftime("%Y-%m-%d %X", time.localtime()))
strs=['www.baidu.com']
for st in strs:
 	if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', st) != None:
  		print 'IP!'
  	else:
  		print 'web'
