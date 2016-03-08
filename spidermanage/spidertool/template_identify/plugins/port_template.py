#!/usr/bin/python
#coding:utf-8

def sipdeal(ip='',port='',name=''):
    print 'this is sipdeal'


def mysql(ip='',port='',name=''):
    head=''
    ans=None
    keywords=''
    hackinfo=''
    import MySQLdb
    con=None
    passwd=['root','123456','admin','','12345']
    for i in passwd:
        try:
            con= MySQLdb.connect(host=ip,user='root',passwd=i)
            hackinfo= ' the password is :'+i
            print ip+hackinfo
            keywords='mysql'
            break;
        except Exception,e:
            if e[0]==2003:
                keywords=''
                print e,e[0]
                break
            if e[0]==1045:
                print ip+'  key is not '+i
                keywords='mysql'

                continue
            else:
                keywords='mysql'
                hackinfo=str(e)
                print e,e[0]
            
        finally:
            if con !=None:
                con.close()
    return head,ans,keywords,hackinfo
    

def empty(ip='',port='',name=''):
    head=None
    ans=None
    keywords=None
    hackinfo=None
    print 'this is empty func'
    
    return head,ans,keywords,hackinfo
 

    

