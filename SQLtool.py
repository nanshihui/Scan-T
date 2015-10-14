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
        def __init__(self):
              temp=config.Config
              self.__host = temp.host
              self.__user=temp.username
              self.__passwd=temp.passwd
              self.__db=temp.database
              self.__port=temp.port
              #print self.__host,self.__user,self.__passwd,self.__db,self.__port
        
	def connectdb(cls):
 		try:
                        cls.__conn=MySQLdb.connect(cls.__host,cls.__user,cls.__passwd,cls.__db,cls.__port)
                        #print self.__host,self.__user,self.__passwd,self.__db,self.__port
   			#cls.__conn=MySQLdb.connect('localhost','root','123456','datap',3306)
    			cls.__cur=cls.__conn.cursor()

    		
    			print "success connet "
		except MySQLdb.Error,e:
     			print "Mysql Error %d: %s" % (e.args[0], e.args[1])
       
	def inserdata(cls):
		
      
   		cls.__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['www','123123','1992-12-12 12:12:12'])
   		
		result=cls.__cur.fetchall()
		for temp in result:
    			print temp[0]
    		
    		cls.__conn.commit()
        def showdata(cls):
                count=cls.__cur.execute('select * from webdata')
                print 'there has %s rows record' % count
	def closedb(cls):
    		cls.__cur.close()
    		cls.__conn.close()
                print 'database has benn closed'