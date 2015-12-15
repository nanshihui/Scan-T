#!/usr/bin/python
#coding:utf-8
import MySQLdb
import config
import time
import datetime
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
import debugdetail as Debug
DBhelp=None
SQLPOOL=None
def getObject():
	global DBhelp
	if DBhelp is None:
		DBhelp=DBmanager()
	return DBhelp
class DBmanager:
	__cur=None
	__conn=None
	__host=''
	__user=''
	__passwd=''
	__db='' 
	__port=3306
	__connection_time=0
	__isconnect=1
	__charset=''
	__cachemin=1
	__cachemax=100
	def __init__(self):
		temp=config.Config
		self.__host = temp.host
		self.__user=temp.username
		self.__passwd=temp.passwd
		self.__db=temp.database
		self.__port=temp.port
		self.__charset=temp.charset
		self.__cachemax=temp.cachemax
		self.__cachemin=temp.cachemin
		self.__conn=None
		self.__cur=None
	def getConnect(self):
		global SQLPOOL
		if SQLPOOL is None:
			SQLPOOL = PooledDB(creator=MySQLdb ,mincached=self.__cachemin , maxcached=0 ,maxshared=0,maxconnections=0,blocking=True,maxusage=0,
									host=self.__host , port=self.__port , user=self.__user , passwd=self.__passwd,
									db=self.__db,use_unicode=False,charset=self.__charset
 									,cursorclass=DictCursor
									)
		return SQLPOOL.connection()
	def connectdb(self):
		try:
			self.__conn=self.getConnect()
# 			if self.__cur is not None:
# 				self.__cur.close()
# 			self.__conn=MySQLdb.connect(self.__host,self.__user,self.__passwd,self.__db,self.__port,charset=self.__charset,cursorclass=DictCursor)
			self.__cur=self.__conn.cursor()
# 			self.__isconnect=1
			self.__isconnect=1
			print "success connet "
		except MySQLdb.Error,e:
			print  '创建连接失败，准备重连  :' +str(e)
			if  self.__connection_time<3 :
				print 'time out ! and reconnect'
				time.sleep(3)
				self.__connection_time=self.__connection_time+1
				self.connectdb()
			else:
				print  'connect fail'
	def closedb(self):
# 		if  self.__isconnect==1:

		if  self.__cur :
			self.__cur.close()
		if  self.__conn:
			self.__conn.close()
# 			self.__isconnect=0
			print 'database has benn closed'
		else:
			print '''has not connet'''
	#searchtableinfo_byparams 输入参数执行对应的查询函数
	#@table 					包含要查询的表，数组
	#@select_params				要显示的列名，数组
	#@request_params     		条件匹配参数，数组
	#@equal_params				每一个与request_params对应相等的数组
	def isdisconnect(self,e):
		if 'MySQL server has gone away' in str(e) or 'cursor closed' in  str(e) or 'Lost connection to MySQL server during query' in str(e):
			return True
		else:
			return False
	def  searchtableinfo_byparams(self,table,select_params=[],request_params=[],equal_params=[],limit='',order='',extra='',command='and'):
		if len(request_params)!=len(equal_params):
			print 'request_params,equals_params长度不相等'
			return (0,0,0,0)
		elif  self.__isconnect==1:

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
						sql=sql+request_params[k]+' = '+equal_params[k]+' '+command+' '
					sql=sql+request_params[request_params_length-1]+' = '+equal_params[request_params_length-1]+'  '
				
				sql+=extra
				if order!='':
					sql+=' order by '+order
				sql+=limit
				sql+=''
# 				print sql
				count=None
				try:
					if self.__cur is not None:
						count=self.__cur.execute(sql)
					else:
						self.connectdb()
						count=self.__cur.execute(sql)
				except MySQLdb.Error,e:
					try:
						if self.isdisconnect(e):
							self.connectdb()
							count=self.__cur.execute(sql)
						else:
							debug=Debug.getObject()
							debug.error(str(e))
							return (0,0,0,0)
					except Exception,e:
						return (0,0,0,0)
				if count>0:
					result=self.__cur.fetchall()
					content=self.__cur.description
					"""
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
					"""
					col=None
					if content is not None:
						col= len(content)
					return result,content,count,col


				else:
					print '没有相关信息'
					return (0,0,0,0)
			except MySQLdb.Error,e:
				print '操作的过程中出现异常 :' +str(e)
				return (0,0,0,0)
		else:
			print '''has not connet'''  
			return (0,0,0,0)
		#self.__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['这个稳重','123123','1992-12-12 12:12:12'])
		#self.__conn.commit()   
	def replaceinserttableinfo_byparams(self,table,select_params,insert_values):
		if len(insert_values)<1 :
			print '没有插入参数'
			return False
		elif  self.__isconnect==1:
			
			try:
				sql='replace into     '+table
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
					return False

# 				print sql
				returnmeg=None
				try:
					returnmeg=self.__cur.executemany(sql,insert_values)
					print '返回的消息：　'+str(returnmeg)
				
					self.__conn.commit()
					if str(returnmeg)=='0':
						print '没有数据变化'
					return True
# 						self.connectdb()
# 						returnmeg=self.__cur.executemany(sql,insert_values)
# 						print '返回的消息：　'+str(returnmeg)		
# 						self.__conn.commit()				
				except MySQLdb.Error,e:
					try:
						if self.isdisconnect(e):
						
							print '进行重连'
							self.connectdb()
							returnmeg=self.__cur.executemany(sql,insert_values)
							print '返回的消息：　'+str(returnmeg)
				
							self.__conn.commit()
							return True
						else:
							debug=Debug.getObject()
							debug.error(str(e))
							return False
					except Exception,e:
						return False
			except MySQLdb.Error,e:
				print  '操作的过程中出现异常:' +str(e)
				return False
		else:
			print '''has not connet'''  
			return False
	def updatetableinfo_byparams(self,table,select_params=[],set_params=[],request_params=[],equal_params=[],extra=''):
		if len(request_params)!=len(equal_params):
			print 'request_params,equals_params长度不相等'
			return False
		elif  self.__isconnect==1:

			try:
				sql='update     '

				length=len(table)

				for j in range(0,length-1):
					sql=sql+table[j]+','
				sql=sql+table[length-1]


				select_params_length=len(select_params)
				if select_params_length>0:

					sql=sql+' set  '
					for k in range(0,select_params_length-1):
						sql=sql+select_params[k]+' = '+set_params[k]+'  , '
					sql=sql+select_params[select_params_length-1]+' = '+set_params[select_params_length-1]+'  '
			
				
				
				request_params_length=len(request_params)
				if request_params_length>0:

					sql=sql+' where '
					for k in range(0,request_params_length-1):
						sql=sql+request_params[k]+' = '+equal_params[k]+' and '
					sql=sql+request_params[request_params_length-1]+' = '+equal_params[request_params_length-1]+'  '
				
				sql+=extra

# 				print sql
				count=None
				try:
					count=self.__cur.execute(sql)
				
					self.__conn.commit()
				except MySQLdb.Error,e:
					try:
						if self.isdisconnect(e):
							self.connectdb()
							count=self.__cur.execute(sql)
				
							self.__conn.commit()
						else:
							debug=Debug.getObject()
							debug.error(str(e))
							return False
					except Exception,e:
						return False
				if count>0:
					return True
				else:
					return False

			except MySQLdb.Error,e:
				print  '操作的过程中出现异常 :' +str(e)
				return False
		else:
			print '''has not connet'''  
			return False	
	def inserttableinfo_byparams(self,table,select_params,insert_values,extra=' ',updatevalue=[]):
		if len(insert_values)<1 :
			print '没有插入参数'
			return False
		elif  self.__isconnect==1:
			
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
					return False
				ulen=len(updatevalue)
				if ulen>0:
					sql+='  on duplicate key update  '
					for o in range(0, ulen-1):
						sql=sql+updatevalue[o]+' =  %s '+'  ,'	
					sql=sql+updatevalue[ulen-1]+'  =%s ' 
				sql+=extra
# 				print sql
				
				
				returnmeg=None
				try:
					returnmeg=self.__cur.executemany(sql,insert_values)
				except MySQLdb.Error,e:
					try:
						if self.isdisconnect(e):
							self.connectdb()
							returnmeg=self.__cur.executemany(sql,insert_values)
						else:
							debug=Debug.getObject()
							debug.error(str(e))	
							return False
					except Exception,e:
						return False
				print '返回的消息：　'+str(returnmeg)
				if returnmeg>0:
					if self.__conn is not None:
						self.__conn.commit()
					return True
				else:
					return False


			except Exception,e:
				print  '操作的过程中出现异常 :' +str(e)
				return False
		else:
			print '''has not connet'''  
			return False
	
		#self.__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['这个稳重','123123','1992-12-12 12:12:12'])
		#self.__conn.commit()   
def formatstring(str):
	return '\''+str+'\''
if __name__ == "__main__":
	SQLtool=DBmanager()
	SQLtool.connectdb()
	localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
	insertdata=[]
#		 insertdata.append((str(ip),port,localtime,str(ans),str(ans),localtime))

#		 self.sqlTool.inserttableinfo_byparams(self.config.porttable,['ip','port','timesearch','detail' ],insertdata)
# 	extra=' on duplicate key update  state=\'open\' , timesearch=\''+localtime+'\''
# 	insertdata.append(('111.111.111.1','1','2014-08-08 11:11:11','str(ans)','str(ans)','2014-08-08 11:11:11'))
#		 self.sqlTool.inserttableinfo_byparams(self.config.porttable,['ip','port','timesearch','detail' ],insertdata)
# 	SQLtool.inserttableinfo_byparams(config.Config.porttable,['ip','port','timesearch','detail'],insertdata,updatevalue=['detail','timesearch'])
	insertdata.append(('110.110.110.110','1',localtime,'open'))
	extra=' on duplicate key update  detail=\'open\' , timesearch=\''+localtime+'\''
	SQLtool.inserttableinfo_byparams(config.Config.porttable,['ip','port','timesearch','detail'],insertdata,extra)
	SQLtool.closedb()
	
	
	