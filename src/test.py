#!/usr/bin/python
import Queue
queue=Queue.Queue(maxsize=1)
queue.put(1,block=False)
def aa():
	try:
		req=queue.get()
#	req=queue.get(block=False)
#	queue.put(1,block=False)
#	queue.put(1,block=False)	
		print 'asd'
		return ''

	except Queue.Empty:
		print '123'
	except Queue.Full:
		print '456'
	except :
		print '789'
	finally:
		print '111'

def we(s):
	print '12ss3'+s
def ss(well,w):
	well(w)
ss(we,'1')