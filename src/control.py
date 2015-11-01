#!/usr/bin/python
#coding:utf-8
from spidertool import searchTask
from spidertool import dealTask
from spidertool import SQLTool
import datetime
if __name__ == "__main__":
	links = [ 'http://www.bunz.edu.cn','http://www.baidu.com','http://www.hao123.com','http://www.cctv.com','http://www.vip.com']
	S_produce= searchTask.searchTask()#表示创建的是线程
	S_produce.set_deal_num(10)
	S_produce.add_work(links)

	S_produce.start_task()

	searchResultSQL=SQLTool.DBmanager()
	searchResultSQL.connectdb()
	F_consume=dealTask.dealTask(0)#参数0表示创建的是进程
	F_consume.set_deal_num(10)
	
	while S_produce.has_work_left():
		v,b=S_produce.get_finish_work()

		searchResultSQL.inserttableinfo_byparams('webdata', ["address","content","meettime"], [(v,b,str(datetime.datetime.now()))])		
		F_consume.add_work(b)
	while True:
		pass




