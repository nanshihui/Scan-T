#!/usr/bin/python

import MySQLdb

class DBmanager:
        __cur=''
        __conn=''
        @classmethod
	def connectdb(cls):
 		try:
   			cls.__conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='datap',port=3306)
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