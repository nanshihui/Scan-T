#!/usr/bin/python
#coding:utf-8
import MySQLdb
import config
import time
class DBmanager:
	__cur=''
	__conn=''
	__host=''
	__user=''
	__passwd=''
	__db='' 
	__port=3306
	__connection_time=0
	__isconnect=0
	__charset=''
	def __init__(self):
		temp=config.Config
		self.__host = temp.host
		self.__user=temp.username
		self.__passwd=temp.passwd
		self.__db=temp.database
		self.__port=temp.port
		self.__charset=temp.charset
	def connectdb(cls):
 		try:
			cls.__conn=MySQLdb.connect(cls.__host,cls.__user,cls.__passwd,cls.__db,cls.__port,charset=cls.__charset)
			#print self.__host,self.__user,self.__passwd,self.__db,self.__port
			#cls.__conn=MySQLdb.connect('localhost','root','123456','datap',3306,charset='utf8')
			cls.__cur=cls.__conn.cursor()
			cls.__isconnect=1
		
			print "success connet "
		except MySQLdb.Error,e:
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])
			if  cls.__connection_time<3:
				print 'time out ! and reconnect'
				time.sleep(3)
				cls.__connection_time=cls.__connection_time+1
				cls.connectdb()
			else:
				print  'connect fail'
	def closedb(cls):
		if  cls.__isconnect==1:
			cls.__cur.close()
			cls.__conn.close()
			cls.__isconnect=0
			print 'database has benn closed'
		else:
			print '''has not connet'''
	#searchtableinfo_byparams 输入参数执行对应的查询函数
	#@table 					包含要查询的表，数组
	#@select_params				要显示的列名，数组
	#@request_params     		条件匹配参数，数组
	#@equal_params				每一个与request_params对应相等的数组
	def  searchtableinfo_byparams(cls,table,select_params,request_params,equal_params):
		if len(request_params)!=len(equal_params):
			print 'request_params,equals_params长度不相等'
			return
		elif  cls.__isconnect==1:

			try:
				sql='select     '
				length=len(select_params)
				if length > 0:

					for j in range(0,length-1):
						sql=sql+select_params[j]+','
					sql=sql+select_params[length-1]
				else:
					sql=sql+'*'
				sql=sql+' from '
				length=len(table)

				for j in range(0,length-1):
					sql=sql+table[j]+','
				sql=sql+table[length-1]
				request_params_length=len(request_params)
				if request_params_length>0:

					sql=sql+' where '
					for k in range(0,request_params_length-1):
						sql=sql+request_params[k]+' = '+equal_params[k]+' and '
					sql=sql+request_params[request_params_length-1]+' = '+equal_params[request_params_length-1]+'  '
				print sql
				count=cls.__cur.execute(sql)

				if count>0:
					result=cls.__cur.fetchall()
					content=cls.__cur.description

					print '相关信息如下：'
					print result
					print content
					for temp in content:
						print temp[0],
					print ''

					for temp in result:
						for i in range(0,len(temp)):
							print temp[i],
						print ''
				else:
					print '没有相关信息'

			except MySQLdb.Error,e:
				print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		else:
			print '''has not connet'''  
		#cls.__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['这个稳重','123123','1992-12-12 12:12:12'])
		#cls.__conn.commit()   

	def inserttableinfo_byparams(cls,table,select_params,insert_values):
		if len(insert_values)<1 :
			print '没有插入参数'
			return
		elif  cls.__isconnect==1:
			
			try:
				sql='insert into     '+table
				length=len(select_params)
				if length > 0:
					sql+='('
					for j in range(0,length-1):
						sql=sql+select_params[j]+','
					sql=sql+select_params[length-1]+')'
					sql=sql+'    '
					sql=sql+' values('	
					for j in range(0,length-1):
						sql=sql+'%s'+','	
					sql=sql+'%s'+')'			
				else:
					return

				print sql
				returnmeg=cls.__cur.executemany(sql,insert_values)
				print '返回的消息：　'+returnmeg
				cls.__conn.commit()


			except MySQLdb.Error,e:
				print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		else:
			print '''has not connet'''  
		#cls.__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['这个稳重','123123','1992-12-12 12:12:12'])
		#cls.__conn.commit()   