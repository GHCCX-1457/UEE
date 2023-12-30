import asyncio
import json
import os

import cv2
import numpy as np
from flask import Blueprint, request
from pandas import concat

from const.R import R
from entity.HZAuth import HZUser
from entity.HZFaceProject import Picicount
from util import TokenUtil
import pandas as pd
#/hzapi/picicount/getPicicount
piciCount = Blueprint('picicount', __name__, url_prefix='/hzapi/picicount')

@piciCount.route('/getPicicount', methods=['GET'])
def getCitycount():
    #分页查询
    page = request.args.get('page',1)
    limit = request.args.get('limit',10)
    #获取数据
    citycount = Picicount.select().paginate(int(page),int(limit))
    #获取数据总数
    count = Picicount.select().count()
    #获取总页数
    pages = count/int(limit)
    if  count%int(limit) != 0:
        pages = int(pages) + 1

    #将数据转换为json
    citycount = [i.__dict__() for i in citycount]
    #返回结果
    return_data = {
      'count': pages,
      'data': citycount
    }

    return R.success(data=return_data,msg='查询成功')

#新增
@piciCount.route('/addPicicount', methods=['POST'])
def addCitycount():
    #获取参数
    address = request.form.get('picis')
    count = request.form.get('count')
    id = request.form.get('id')
    #新增
    Picicount.create(picis=address,count=count,id=id)
    #返回结果
    return R.success(msg='新增成功')

#修改
@piciCount.route('/updatePicicount', methods=['POST'])
def updateCitycount():
#获取参数
    address = request.form.get('picis')
    count = request.form.get('count')
    id = request.form.get('id')
    #修改
    Picicount.update(picis=address,count=count).where(Picicount.id == id).execute()
    #返回结果
    return R.success(msg='修改成功')

#删除
@piciCount.route('/deletePicicount', methods=['DELETE'])
def deleteCitycount():
    #获取参数
    id = request.args.get('id')
    #删除
    Picicount.delete().where(Picicount.id == id).execute()
    #返回结果
    return R.success(msg='删除成功')

