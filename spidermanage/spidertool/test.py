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
# debug=Debug.getObject()
# debug.error("asd")
print 'this is the test file please ignore it'

def aaaa():
	from logger import initLog
	logger = initLog('portScantask.log', 2, True,'asd')

	logger.info('%s 端口扫描　执行任务中%s', 1,2)

import json
param='{"admin":1,"user":"asd"}'
d = json.loads(param)
print d.keys()
param='as'
if param:
	print 'asdasd'
from funcmemo import memoize
@memoize
def fibonacci(n):
    if n < 2: return n
    print n
    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci(25)

def fib(max):  
    a, b = 1, 1  
    while a < max:  
        yield a #generators return an iterator that returns a stream of values.  
        print str(a)+'               111111111'
        a+=1
for n in fib(15):  
    pass
a={}
a['a']='1'
if a.get('a',''):
	print 1














