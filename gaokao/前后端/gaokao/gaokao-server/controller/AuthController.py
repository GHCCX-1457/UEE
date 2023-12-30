import asyncio
import os

from flask import Blueprint, request

from const.R import R
from entity.HZAuth import HZUser
from util import TokenUtil, RedisUtil

auth = Blueprint('auth', __name__, url_prefix='/hzapi/auth')

# 登陆
@auth.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    try:
        user = HZUser.filter(username=username)[0]
    except Exception as e:
        user = None
    if user:
        if user.password == password:
            access_token = TokenUtil.create_token(username=username)
            RedisUtil.set_key(access_token, username, time=60 * 60 * 24 * 7)
            result = {
                'access_token': access_token,
                'user_id': user.id,
                'name': user.name,
            }
            return R.success(data=result,msg='登陆成功')
        else:
            return R.fail(msg='密码错误')
    else:
        return R.fail(msg='用户不存在')
    #将用户名存入redis


# 注册
@auth.route('/register', methods=['POST', 'GET'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    user = HZUser.filter(username=username)
    try:
        user = HZUser.filter(username=username)[0]
    except Exception as e:
        user = None
    if user:
        return R.fail(msg='用户已存在')
    HZUser.create(username=username, password=password)
    return R.success(msg='注册成功')


# 忘记密码
@auth.route('/forget-password', methods=['POST', 'GET'])
def forget():
    username = request.json.get('username')
    oldpassword = request.json.get('oldpassword')
    password = request.json.get('password')
    try:
        user = HZUser.filter(username=username)[0]
    except Exception as e:
        user = None
    if user:
        if user.password != oldpassword:
            return R.fail(msg='旧密码错误')
        user.password = password
        user.save()
        return R.success(msg='修改成功')
    else:
        return R.fail(msg='用户不存在')

# 修改个人信息
@auth.route('/update', methods=['POST'])
def update():
    '''
    修改个人信息
    ---
    tags:
        - 修改个人信息
    parameter:
        -   name: name
            in: formData
            type: string
            required: true
            description: 姓名
        -   name: phone
            in: formData
            type: string
            required: true
            description: 电话
        -   name: address
            in: formData
            type: string
            required: true
            description: 地址
        -   name: email
            in: formData
            type: string
            required: true
            description: 邮箱
    '''
    name = request.json.get('name')
    phone = request.json.get('phone')
    address = request.json.get('address')
    email = request.json.get('email')
    authToken = request.headers.get('Authorization')
    username = TokenUtil.get_username(token=authToken)
    if username == None:
        return R.fail(msg='非法请求')
    try:
        user = HZUser.get(HZUser.username == username)
    except:
        return R.fail(msg='用户不存在')
    if user:
        user.name = name
        user.phone = phone
        user.address = address
        user.email = email
        user.save()
        return R.success(msg='修改成功')
    else:
        return R.fail(msg='用户不存在')


# 获取当前登录的用户信息
@auth.route('/getInfo', methods=['GET'])
def getInfo():
    '''
    获取当前登录的用户信息
    ---
    tags:
        - 获取当前登录的用户信息
    '''
    authToken = request.headers.get('Authorization')
    #            RedisUtil.set_key(access_token, username, time=60 * 60 * 24 * 7)
    username = TokenUtil.get_username(token=authToken)
    if username == None:
        return R.fail(msg='非法请求')
    try:
        user = HZUser.get(HZUser.username == username)
    except:
        return R.fail(msg='用户不存在')
    if user:
        result = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'phone': user.phone,
            'address': user.address,
            'email': user.email,
            'role': user.role,
        }

        return R.success(data=result, msg='获取成功')
    else:
        return R.fail(msg='用户不存在')