#!/usr/bin/python
#coding:utf-8
import Queue
import time
import re
from subprocess import Popen, PIPE
import os
import debugdetail as Debug
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
f = open(r'iparea.json')
temp=f.readlines()
f.close()
# for i in range(0,5):
# 	print i
a='12345'
def asd(*a):
	return a
sdf=(6,7)
print asd(sdf)


def p(i):
	print i 

def fun_var_args_call(arg1, arg2, arg3,arg4=1):  
    print "arg1:", arg1  
    print "arg2:", arg2  
    print "arg3:", arg3  
    arg1(arg2)
    print arg4
  
kwargs = {"arg3": 3, "arg2": "two","arg1":p} # dictionary  
fun_var_args_call(**kwargs)
class alotod:
	def __init__(self):
		self.oo=1
	def temp(self,name):
		print name
	def fuc(self):
		print '123'
	def ad(self):
		return 1
v=alotod()		
print v.temp.__name__		
		
# k=getattr(v, 'ad','1')()
try:
	try:
		pp=1
		pp[2]=''
	except Exception,e:
		print 2222
except Exception,e:
	print 12222
e='askjdajksnd Masdnk'
if 'M' in str(e):
	print 123123
debug=Debug.getObject()
debug.error("asd")
