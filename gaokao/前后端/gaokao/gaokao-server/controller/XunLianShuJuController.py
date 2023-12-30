import asyncio
import json
import os
import joblib
import cv2
import numpy as np
from flask import Blueprint, request
from pandas import concat

from const.R import R
from entity.HZAuth import HZUser
from entity.HZFaceProject import Xunlianshuju
from util import TokenUtil
import pandas as pd
#/hzapi/xunlianshuju/getAllXunlianshujuForBar
xunlianshuju = Blueprint('xunlianshuju', __name__, url_prefix='/hzapi/xunlianshuju')

@xunlianshuju.route('/getXunlianshuju', methods=['GET'])
def getXunlianshuju():
    #分页查询
    page = request.args.get('page',1)
    limit = request.args.get('limit',10)
    #获取数据
    xunlianshuju = Xunlianshuju.select().paginate(int(page),int(limit))
    #获取数据总数
    count = Xunlianshuju.select().count()
    #获取总页数
    pages = count/int(limit)
    if  count%int(limit) != 0:
        pages = int(pages) + 1

    #将数据转换为json
    xunlianshuju = [i.__dict__() for i in xunlianshuju]
    #返回结果
    return_data = {
      'count': pages,
      'data': xunlianshuju
    }

    return R.success(data=return_data,msg='查询成功')

#新增
@xunlianshuju.route('/addXunlianshuju', methods=['POST'])
def addXunlianshuju():
#获取参数
    score = request.form.get('score')
    count = request.form.get('count')
    id = request.form.get('id')
    #新增
    Xunlianshuju.create(score=score,count=count,id=id)
    #返回结果
    return R.success(msg='新增成功')

#修改
@xunlianshuju.route('/updateXunlianshuju', methods=['POST'])
def updateXunlianshuju():
    #获取参数
# like_school
# wenke_school
# chinese
# math
# english
# physics
# chemistry
# biology
# politics
# history
# geography
# location
# time
# wenke_score
# like_score
# id
    like_school = request.form.get('like_school')
    wenke_school = request.form.get('wenke_school')
    chinese = request.form.get('chinese')
    math = request.form.get('math')
    english = request.form.get('english')
    physics = request.form.get('physics')
    chemistry = request.form.get('chemistry')
    biology = request.form.get('biology')
    politics = request.form.get('politics')
    history = request.form.get('history')
    geography = request.form.get('geography')
    location = request.form.get('location')
    time = request.form.get('time')
    wenke_score = request.form.get('wenke_score')
    like_score = request.form.get('like_score')
    id = request.form.get('id')
    #修改
    Xunlianshuju.update(like_school=like_school,wenke_school=wenke_school,chinese=chinese,math=math,english=english,physics=physics,chemistry=chemistry,
                        biology=biology,politics=politics,history=history,geography=geography,location=location,time=time,wenke_score=wenke_score,like_score=like_score).where(Xunlianshuju.id == id).execute()
    #返回结果
    return R.success(msg='修改成功')


#删除
@xunlianshuju.route('/deleteXunlianshuju', methods=['DELETE'])
def deleteXunlianshuju():
#获取参数
    id = request.args.get('id')
    #删除
    Xunlianshuju.delete().where(Xunlianshuju.id == id).execute()
    #返回结果
    return R.success(msg='删除成功')


#查询所有数据
@xunlianshuju.route('/getAllXunlianshujuForBar', methods=['GET'])
def getAllXunlianshujuForBar():
    #分页
    page = request.args.get('page',1)
    limit = request.args.get('limit',10)
    #获取数据
    xunlianshuju = Xunlianshuju.select().paginate(int(page),int(limit))
    #获取数据总数
    count = Xunlianshuju.select().count()
    #获取总页数
    pages = count/int(limit)
    if  count%int(limit) != 0:
        pages = int(pages) + 1

    #将数据转换为json
    xunlianshuju = [i.__dict__() for i in xunlianshuju]

    print(xunlianshuju)
    x=[]
    y=[]
    for i in xunlianshuju:
        x.append(i['time'])
        y.append(i['like_score'])

    #返回结果
    return_data = {
        'count': pages,
        'x': x,
        'y': y

    }
    return R.success(data=return_data,msg='查询成功')




