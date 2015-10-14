#!/usr/bin/python

import MySQLdb
import config
class DBmanager:
        __cur=''
        __conn=''
        __host=''
        __user=''
        __passwd=''
        __db=''
        __port=3306
        def __init__(self,):
              self.__host = config.Config.host
              self.__user=config.Config.username
              self.__passwd=config.Config.passwd
              self.__db=config.Config.database
              self.__port=config.Config.port
        @classmethod
	def connectdb(cls):
 		try:
                        #cls.__conn=MySQLdb.connect(cls.__host,cls.__user,cls.__passwd,cls.__db,cls.__port)
   			cls.__conn=MySQLdb.connect('localhost','root','123456','datap',3306)
    			cls.__cur=cls.__conn.cursor()

    		
    			print "success connet "
		except MySQLdb.Error,e:
     			print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        @classmethod
	def inserdata(cls):
		count=__cur.execute('select * from webdata')
		print 'there has %s rows record' % count
      
   		cls.__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['www','123123','1992-12-12 12:12:12'])
   		
		result=cls.__cur.fetchall()
		for temp in result:
    			print temp[0]
    		
    		cls.__conn.commit()
        @classmethod
	def closedb(cls):
    		cls.__cur.close()
    		cls.__conn.close()