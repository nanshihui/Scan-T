#!/usr/bin/python
#coding:utf-8
try:
    from plugins import port_template,rsyncdeal,sshdeal,ftp_weakpass
    portFunc = {
         '3306':port_template.mysql,
         '873':rsyncdeal.rsync,
         '22':sshdeal.ssh2,
        '21':ftp_weakpass.ftpdeal
 }
except Exception,e:
    print e