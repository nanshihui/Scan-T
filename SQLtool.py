#!/usr/bin/python
# -*- coding:utf8 -*-
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
              #print self.__host,self.__user,self.__passwd,self.__db,self.__port
        
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
	def inserdata(cls):
		if  cls.__isconnect==1:
      
   		         cls.__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['zz','123123','1992-12-12 12:12:12'])
   		         cls.__conn.commit()
                else:
                        print '''has not connet'''
        def showdata(cls):
                if  cls.__isconnect==1:

                          count=cls.__cur.execute('select * from webdata')
                          print 'there has %s rows record' % count
                          result=cls.__cur.fetchall()
                          for temp in result:
                                  print temp[0]
                else:
                          print '''has not connet'''
	def closedb(cls):
                if  cls.__isconnect==1:
    		          cls.__cur.close()
    		          cls.__conn.close()
                          cls.__isconnect=0
                          print 'database has benn closed'
                else:
                          print '''has not connet'''

                          