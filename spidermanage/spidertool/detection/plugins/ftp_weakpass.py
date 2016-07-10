#!/usr/bin/python
#coding:utf-8

import ftplib, socket, re, sys, time





def ftp_anon(host,port='21'):
    try:
        print '\n[+] 测试匿名登陆……\n'
        ftp = ftplib.FTP()
        ftp.connect(host, int(port), 10)
        ftp.login()
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[+] 匿名登陆成功……'
        return True
    except ftplib.all_errors:
        print '\n[-] 匿名登陆失败……'
        return False


def ftp_crack(host, user, pwd,port='21'):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, int(port), 10)
        ftp.login(user, pwd)
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[+] 破解成功，用户名：' + user + ' 密码：' + pwd
        return True,'ftp password is '+user+':'+pwd
    except ftplib.all_errors:
        return False,''

def ftpdeal(ip='',port='21',name='',productname=''):
    ans=None
    head=''
    hackinfo=''
    keywords='ftp'
    if ftp_anon(ip,port):
        hackinfo='allow annoymous ftp'
        return head,ans,'ftp',hackinfo
    else:
#         userlist=['root','123456','admin','12345','111111','password','123123','1234','12345678','123456789','sa','test','Administrator','ftp']
# 
# 
#         passlist=['root','123456','admin','','12345','111111','password','123123','1234','12345678','123456789','sa','ftp',
#             'abc123','qwerty','test','','123']
        userlist=['admin','test']


        passlist=['admin','test']
        for user in userlist:
            for pwd in passlist:
                print 'ftp尝试'+user+':'+pwd
                result,hackinfo=ftp_crack(ip, user, pwd,port)
                if result:
                    return head,ans,keywords,hackinfo
        return head,ans,keywords,hackinfo