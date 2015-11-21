#!/usr/bin/python
#coding:utf-8
import Queue
import time
import re
from subprocess import Popen, PIPE
import os
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
# returnmsg =subprocess.call(["ls", "-l"],shell=True)
path=os.getcwd()
# p= Popen(" ./zmap -B 10M -p 80 -n 10000  -q -O json", stdout=PIPE, shell=True,cwd=path+'/zmap-2.1.0/src')
p= Popen(" ./zmap -B 10M -p 80 -n 100000 -o results.txt", stdout=PIPE, shell=True,cwd=path+'/zmap-2.1.0/src')

p.wait()

returnmsg=p.stdout.read() 
print returnmsg












 
