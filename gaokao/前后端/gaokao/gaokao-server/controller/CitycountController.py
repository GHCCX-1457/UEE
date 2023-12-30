import asyncio
import json
import os

import cv2
import numpy as np
from flask import Blueprint, request
from pandas import concat

from const.R import R
from entity.HZAuth import HZUser
from entity.HZFaceProject import Citycount
from util import TokenUtil
import pandas as pd

citycount = Blueprint('citycount', __name__, url_prefix='/hzapi/citycount')

@citycount.route('/getCitycount', methods=['GET'])
def getCitycount():
    #分页查询
    page = request.args.get('page',1)
    limit = request.args.get('limit',10)
    #获取数据
    citycount = Citycount.select().paginate(int(page),int(limit))
    #获取数据总数
    count = Citycount.select().count()
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
@citycount.route('/addCitycount', methods=['POST'])
def addCitycount():
    #获取参数
    address = request.form.get('address')
    count = request.form.get('count')
    id = request.form.get('id')
    #新增
    Citycount.create(address=address,count=count,id=id)
    #返回结果
    return R.success(msg='新增成功')

#修改
@citycount.route('/updateCitycount', methods=['POST'])
def updateCitycount():
#获取参数
    address = request.form.get('address')
    count = request.form.get('count')
    id = request.form.get('id')
    #修改
    Citycount.update(address=address,count=count).where(Citycount.id == id).execute()
    #返回结果
    return R.success(msg='修改成功')

#删除
@citycount.route('/deleteCitycount', methods=['DELETE'])
def deleteCitycount():
    #获取参数
    id = request.args.get('id')
    #删除
    Citycount.delete().where(Citycount.id == id).execute()
    #返回结果
    return R.success(msg='删除成功')

