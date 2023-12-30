import json

import redis



redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=0, max_connections=1000, decode_responses=True)

'''
redis 工具类
'''

def get_key(key):
    '''
    获取key
    '''
    r = redis.Redis(connection_pool=redis_pool)
    return r.get(key)

def set_key(key, value, time=None):
    '''
    设置key
    '''
    r = redis.Redis(connection_pool=redis_pool)
    r.set(key, value, time)

def delete_key(key):
    '''
    删除key
    '''
    r = redis.Redis(connection_pool=redis_pool)
    r.delete(key)

def get_keys(pattern):
    '''
    获取所有key
    '''
    r = redis.Redis(connection_pool=redis_pool)
    return r.keys(pattern)

def get_all_keys(self):
    '''
    获取所有key
    '''
    r = redis.Redis(connection_pool=redis_pool)
    return r.keys('*')

def get_all_values(self):
    '''
    获取所有value
    '''
    r = redis.Redis(connection_pool=redis_pool)
    return r.values()

def get_all_items(self):
    '''
    获取所有item
    '''
    r = redis.Redis(connection_pool=redis_pool)
    return r.items()

def get_all(self):
    '''
    获取所有
    '''
    r = redis.Redis(connection_pool=redis_pool)
    return r.get_all()
