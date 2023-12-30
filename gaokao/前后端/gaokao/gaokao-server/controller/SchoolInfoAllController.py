import asyncio
import json
import os

import cv2
import numpy as np
from flask import Blueprint, request
from pandas import concat

from const.R import R
from entity.HZAuth import HZUser
from entity.HZFaceProject import Schoolinfoall
from util import TokenUtil
import pandas as pd


#/hzapi/schoolinfoall/getSchoolinfoallById
schoolinfoall = Blueprint('schoolinfoall', __name__, url_prefix='/hzapi/schoolinfoall')

@schoolinfoall.route('/getSchoolinfoallById', methods=['GET'])
def getSchoolinfoallById():
    id = request.args.get('id')

    #获取数据
    try:
        schoolinfoall = Schoolinfoall.select().where(Schoolinfoall.schoolid == id)
    except Exception as e:
        return R.error(msg='查询失败')
    #将数据转换为json
    schoolinfoall = [i.__dict__() for i in schoolinfoall]
    #返回结果
    return_data = {
        'data': schoolinfoall
    }

    return R.success(data=return_data,msg='查询成功')