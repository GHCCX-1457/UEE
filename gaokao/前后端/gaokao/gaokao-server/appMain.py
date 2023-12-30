from flasgger import Swagger
from flask import Flask, request
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

from const.R import R
from controller.AuthController import auth
from controller.CitycountController import citycount
from controller.PiciCountController import piciCount
from controller.ShoolDateController import schooldate
from controller.ScoreCountController import scorecount
from controller.XunLianShuJuController import xunlianshuju
from controller.SchoolInfoAllController import schoolinfoall
# from controller.StudentController import student
# from controller.TeacherController import teacher
from entity.HZAuth import HZUser
from entity.HZFaceProject import *
from util import RedisUtil, TokenUtil

app = Flask(__name__)
# app.register_blueprint(teacher)
# app.register_blueprint(student)
app.register_blueprint(auth)
app.register_blueprint(citycount)
app.register_blueprint(piciCount)
app.register_blueprint(schooldate)
app.register_blueprint(scorecount)
app.register_blueprint(xunlianshuju)
app.register_blueprint(schoolinfoall)#Q:为什么要注册蓝图？    A:蓝图是什么？蓝图是一种组织代码的方式，将代码按照功能进行分组，方便管理
admin = Admin(app, name='HZAdmin', template_mode='bootstrap3')
Swagger(app)

def initDataBase():
    print('##################initDataBase##################')
    if HZUser.table_exists()==False:
        HZUser.create_table()
    # if HZClass.table_exists()==False:
    #     HZClass.create_table()
    # if HZAttendance.table_exists()==False:
    #     HZAttendance.create_table()
    # if HZClassStudent.table_exists()==False:
    #     HZClassStudent.create_table()
    # if HZStudentFace.table_exists()==False:
    #     HZStudentFace.create_table()
    print('##################initDataBase##################')

def initAdmin():
    print('##################initAdmin##################')
    admin.add_view(ModelView(HZUser,name='用户管理'))
    # admin.add_view(ModelView(HZClass,name='班级管理'))
    # admin.add_view(ModelView(HZAttendance,name='考勤管理'))
    # admin.add_view(ModelView(HZClassStudent,name='班级学生管理'))
    # admin.add_view(ModelView(HZStudentFace,name='学生人脸管理'))
    print('##################initAdmin##################')

@app.before_request
def before():
    print('##################before##################')
    # 设置登录验证
    if request.path.startswith('/hzapi/auth') == False | \
            request.path.startswith('/static') == False | \
            request.path.startswith('/apidocs') == False | \
            request.path.startswith('/flasgger_static') == False | \
            request.path.startswith('/apispec') == False | \
            request.path.startswith('/admin') == False | \
            request.path.startswith('/hzapi/citycount') == False | \
            request.path.startswith('/hzapi/picicount') == False | \
            request.path.startswith('/hzapi/schooldate') == False | \
            request.path.startswith('/hzapi/scorecount') == False | \
            request.path.startswith('/hzapi/xunlianshuju') == False | \
            request.path.startswith('/hzapi/schoolinfoall') == False :
        #Q:request.path.startswith('/hzapi/auth') 是什么意思？    A:判断请求路径是否以/hzapi/auth开头
        # 验证token
        authToken = request.headers.get('Authorization')
        print(authToken)
        if authToken == None:
            return R.fail(msg='请先登录')
        else:
            # 验证token
            auth = RedisUtil.get_key(key=authToken)
            if auth == None:
                # 424 Failed Dependency
                return R.fail(msg='Token不存在，请重新登录')

            else:
                check = TokenUtil.check_token(token=authToken)
                if check['code'] == 200:
                    pass
                else:
                    return check
    print('##################before##################')

initDataBase()
initAdmin()

if __name__ == '__main__':
    app.run()

