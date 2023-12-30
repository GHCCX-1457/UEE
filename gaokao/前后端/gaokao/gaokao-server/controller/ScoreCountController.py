import asyncio
import json
import os

import cv2
import numpy as np
from flask import Blueprint, request
from pandas import concat

from const.R import R
from entity.HZAuth import HZUser
from entity.HZFaceProject import Scorecount
from util import TokenUtil
import pandas as pd
#/hzapi/scorecount/getAllScorecountForPie
scorecount = Blueprint('scorecount', __name__, url_prefix='/hzapi/scorecount')

@scorecount.route('/getScorecount', methods=['GET'])

def getScorecount():
    #分页查询
    page = request.args.get('page',1)
    limit = request.args.get('limit',10)
    #获取数据
    scorecount = Scorecount.select().paginate(int(page),int(limit))
    #获取数据总数
    count = Scorecount.select().count()
    #获取总页数
    pages = count/int(limit)
    if  count%int(limit) != 0:
        pages = int(pages) + 1

    #将数据转换为json
    scorecount = [i.__dict__() for i in scorecount]
    #返回结果
    return_data = {
      'count': pages,
      'data': scorecount
    }

    return R.success(data=return_data,msg='查询成功')

#新增
@scorecount.route('/addScorecount', methods=['POST'])
def addScorecount():
#获取参数
    score = request.form.get('score')
    count = request.form.get('count')
    id = request.form.get('id')
    #新增
    Scorecount.create(score=score,count=count,id=id)
    #返回结果
    return R.success(msg='新增成功')

#修改
@scorecount.route('/updateScorecount', methods=['POST'])
def updateScorecount():
#获取参数
    score = request.form.get('score')
    count = request.form.get('count')
    id = request.form.get('id')
    #修改
    Scorecount.update(score=score,count=count,id=id)
    #返回结果
    return R.success(msg='修改成功')

#删除
@scorecount.route('/deleteScorecount', methods=['DELETE'])
def deleteScorecount():
#获取参数
    id = request.args.get('id')
    #删
    Scorecount.delete().where(Scorecount.id == id).execute()
    #返回结果
    return R.success(msg='删除成功')


#返回所有数据
@scorecount.route('/getAllScorecountForPie', methods=['GET'])
def getAllScorecountForPie():
    #获取数据
    scorecount = Scorecount.select()
    #将数据转换为json
    scorecount = [i.__dict__() for i in scorecount]
    return_list = []

    for i in scorecount:
        data_count = {
            'value':i['count'],
            'name':i['score']
        }
        return_list.append(data_count)


    #返回结果
    return R.success(data=return_list,msg='查询成功')