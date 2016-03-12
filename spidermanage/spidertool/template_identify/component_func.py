#!/usr/bin/python
#coding:utf-8
from plugins import port_template,rsyncdeal,sshdeal
componentFunc = {
                 'mysql':port_template.mysql,
                 'rsync':rsyncdeal.rsync,
                 'ssh':sshdeal.ssh2
 } 