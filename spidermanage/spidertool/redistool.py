#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
#通过python操作redis缓存

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
#host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379

r = redis.Redis(connection_pool=pool)


def set(obj):
    r.set('foo', 'Bar')

def get(obj):
    r.get(obj)
