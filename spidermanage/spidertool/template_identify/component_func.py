#!/usr/bin/python
#coding:utf-8
from plugins import port_template,rsyncdeal
componentFunc = {
                 'mysql':port_template.mysql,
                 'rsync':rsyncdeal.rsync
 } 