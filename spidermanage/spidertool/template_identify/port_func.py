#!/usr/bin/python
#coding:utf-8
from plugins import port_template,rsyncdeal,sshdeal
portFunc = {
         '3306':port_template.mysql,
         '873':rsyncdeal.rsync,
         '22':sshdeal.ssh2
 }