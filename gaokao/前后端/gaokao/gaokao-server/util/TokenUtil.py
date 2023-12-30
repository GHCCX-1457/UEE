import time

import jwt

from const.R import R
from util import RedisUtil

SECRET_KEY = 'hzsystem_secret_key'

def create_token(username):
    '''
    创建token
    '''
    token_text = {
        'username': username,
        'time': time.time(),
        'out_time': time.time() + 60 * 60 * 24,
    }
    token = jwt.encode(token_text, SECRET_KEY, algorithm='HS256')
    return token

def check_token(token):
    '''
    检查token
    '''
    try:
        token_text = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if token_text['out_time'] < time.time():
            return R.fail(msg='Token已过期，请重新登录')
        else:
            return R.success(msg='Token验证通过')
    except Exception as e:
        return R.fail(msg='Token验证失败，请重新登录')

def get_username(token):
    '''
    获取用户名
    '''
    try:
        username = RedisUtil.get_key(key=token)
        return username
    except Exception as e:
        return None
