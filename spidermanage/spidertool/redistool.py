#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,datetime
#通过python操作redis缓存
redisinstance=None
try:
    if redisinstance is None:
        import redis
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
#host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379

        redisinstance = redis.Redis(connection_pool=pool)

except Exception,e:
    print e




def getObject():
    return redisinstance





def get(key):
    if redisinstance is None:
        return None
    prev_topicList_redis = redisinstance.get(key)
    prev_topicList=prev_topicList_redis
    try:
    # read from redis, but the prev_topicList is a dict rather than a object
        prev_topicList = json.loads(prev_topicList_redis)
    except Exception,e:
        print e
        pass
    return prev_topicList


def set(key,value):
    if redisinstance is None:
        return
    topicList_json=value
    try:
    # covert the object to the json format
        topicList_json = json.dumps(value, default=jdefault, indent=2, ensure_ascii=False).encode('utf-8')
    except Exception,e:
        print e
        pass
    redisinstance.set(key, topicList_json)

def jdefault(o):
    if isinstance(o, datetime):
         return o.isoformat()

    return o.__dict__
