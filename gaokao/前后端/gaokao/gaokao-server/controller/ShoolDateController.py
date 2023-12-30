import asyncio
import json
import os

import cv2
import joblib
import numpy as np
from flask import Blueprint, request
from pandas import concat

from const.R import R
from entity.HZAuth import HZUser
from entity.HZFaceProject import Schooldate
from util import TokenUtil
import pandas as pd

schooldate = Blueprint('schooldate', __name__, url_prefix='/hzapi/schooldate')

@schooldate.route('/getSchooldate', methods=['GET'])
def getCitycount():
    #分页查询
    page = request.args.get('page',1)
    limit = request.args.get('limit',10)
    #获取数据
    citycount = Schooldate.select().paginate(int(page),int(limit))
    #获取数据总数
    count = Schooldate.select().count()
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
@schooldate.route('/addSchooldate', methods=['POST'])
def addCitycount():
    # 'id': self.id,
    # 'schoolid': self.schoolid,
    # 'name': self.name,
    # 'address': self.address,
    # 'info': self.info,
    # 'img': self.img,
    # 'score': self.score,
    # 'weici': self.weici,
    # 'school_types': self.school_types,
    # 'school_pici': self.school_pici,
    # 'school_leibie': self.school_leibie
    #获取参数
    schoolid = request.form.get('schoolid')
    name = request.form.get('name')
    address = request.form.get('address')
    info = request.form.get('info')
    img = request.form.get('img')
    score = request.form.get('score')
    weici = request.form.get('weici')
    school_types = request.form.get('school_types')
    school_pici = request.form.get('school_pici')
    school_leibie = request.form.get('school_leibie')
    #新增
    Schooldate.create(schoolid=schoolid,name=name,address=address,info=info,img=img,score=score,weici=weici,school_types=school_types,school_pici=school_pici,school_leibie=school_leibie)
    #返回结果
    return R.success(msg='新增成功')

#修改
@schooldate.route('/updateSchooldate', methods=['POST'])
def updateCitycount():
#获取参数
    schoolid = request.form.get('schoolid')
    name = request.form.get('name')
    address = request.form.get('address')
    info = request.form.get('info')
    img = request.form.get('img')
    score = request.form.get('score')
    weici = request.form.get('weici')
    school_types = request.form.get('school_types')
    school_pici = request.form.get('school_pici')
    school_leibie = request.form.get('school_leibie')
    id = request.form.get('id')
    #修改
    Schooldate.update(schoolid=schoolid,name=name,address=address,info=info,img=img,score=score,weici=weici,school_types=school_types,school_pici=school_pici,school_leibie=school_leibie).where(Schooldate.id == id).execute()
    #返回结果
    return R.success(msg='修改成功')

#删除
@schooldate.route('/deleteSchooldate', methods=['DELETE'])
def deleteCitycount():
    #获取参数
    id = request.args.get('id')
    #删除
    Schooldate.delete().where(Schooldate.id == id).execute()
    #返回结果
    return R.success(msg='删除成功')


#根据地区查询学校
@schooldate.route('/getSchooldateByAddress', methods=['GET'])#Q：为什么会404？    A：因为没有写路由 /hzapi/schooldate/getSchooldateByAddress 但是我写了 /hzapi/schooldate/getSchooldateByAddress/  所以会404
def getSchooldateByAddress():
    #分页查询
    page = request.args.get('page',1)
    limit = request.args.get('limit',5)
    address = request.args.get('address')
    #获取数据
    citycount = Schooldate.select().where(Schooldate.address.contains(address)).paginate(int(page), int(limit))#模糊查询
    #获取数据总数
    count = Schooldate.select().where(Schooldate.address.contains(address)).count()
    #获取总页数
    pages = int(count/int(limit))
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

#获取前端的预测元数据（post）
@schooldate.route('/getPredictData', methods=['POST'])
def getPredictData():
    #获取参数
    chinese = request.form.get('chinese')
    english = request.form.get('english')
    math = request.form.get('math')
    all = request.form.get('all')

    a1= int(all)/3
    a2 = int(all)/3
    a3 = int(all)/3

    #加载模型
    estimator = joblib.load('static/model/xianxinmoxing/linear.pkl')
    #预测
    result = estimator.predict([[chinese,english,math,a1,a2,a3]])
    yucezhi = int(result[0])
    #根据预测结果查询学校名字

    # 获取最大值
    max = yucezhi + 50
    # 获取最小值
    min = yucezhi
    print(min)
    # 查询数据库，排序
    if max>700:
        max = 680
        min= 550
    if max>550:
        schoolname = Schooldate.select().where(Schooldate.score.between(min, max)).order_by(Schooldate.score.desc())
    if min<330:
        schoolname = Schooldate.select().where(Schooldate.score.between(min, max)).order_by(Schooldate.score.asc())
    if min<200:
        max = 350
        min = 250
    schoolname = Schooldate.select().where(Schooldate.score.between(min, max)).order_by(Schooldate.score.asc())
    print(schoolname)
    #将数据转换为json
    schoolname = [i.__dict__() for i in schoolname][0]
    print(schoolname)


    return R.success(data=schoolname,msg='预测成功')


#根据id查询学校getSchooldateById
@schooldate.route('/getSchooldateById', methods=['GET'])
def getSchooldateById():
    #获取参数
    id = request.args.get('id')
    #获取数据
    citycount = Schooldate.select().where(Schooldate.schoolid == id)
    #将数据转换为json
    citycount = [i.__dict__() for i in citycount][0]
    #返回结果
    return R.success(data=citycount,msg='查询成功')

#预测录取概率（post）
@schooldate.route('/getPredictDataBySchool', methods=['POST'])
def getPredictDataBySchool():
      #获取参数
        schoolscore= request.form.get('schoolscore')
        chinese = request.form.get('chinese')
        english = request.form.get('english')
        math = request.form.get('math')
        all = request.form.get('all')
        #加载模型
        estimator = joblib.load('./static/model/jueceshumoxing/dtc.pkl')
        #预测
        result = estimator.predict([[chinese,english,math,all,schoolscore]])
        yucezhi = int(result[0])

        return R.success(data=yucezhi,msg='预测成功')

