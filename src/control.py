#!/usr/bin/python
#coding:utf-8
from spidertool import searchTask
from spidertool import dealTask
if __name__ == "__main__":
	links = [ 'http://www.bunz.edu.com','http://www.baidu.com','http://www.hao123.com','http://www.cctv.com','http://www.vip.com']
	S_produce= searchTask.searchTask()
	S_produce.set_deal_num(10)
	S_produce.add_work(links)

	S_produce.start_task()

	F_consume=dealTask.dealTask()
	F_consume.set_deal_num(10)
	while S_produce.has_work_left():
		v,b=S_produce.get_finish_work()
		
		F_consume.add_work(b)
	while True:
		pass




