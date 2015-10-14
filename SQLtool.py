#!/usr/bin/python

import MySQLdb

class DBmanager:
        __cur=''
        __conn=''
	def connectdb():
 		try:
   			__conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='datap',port=3306)
    			__cur=__conn.cursor()

    		
    			print "success connet "
		except MySQLdb.Error,e:
     			print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	def inserdata():
		count=__cur.execute('select * from webdata')
		print 'there has %s rows record' % count
      
   		__cur.execute('insert into webdata(address,content,meettime) values(%s,%s,%s)',['www','123123','1992-12-12 12:12:12'])
   		
		result=__cur.fetchall()
		for temp in result:
    			print temp[0]
    		
    		__conn.commit()
	def closedb():
    		__cur.close()
    		__conn.close()