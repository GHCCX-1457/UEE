from peewee import CharField

from entity.BaseEntity import BaseEntity


#城市统计
class Citycount(BaseEntity):
    #城市
    address = CharField(max_length=35)
    #数量
    count = CharField(max_length=35)

    class Meta:
        table_name = 'city_count'

    def __str__(self):
        return self.address

    def __dict__(self):
        return {
            'id': self.id,
            'address': self.address,
            'count': self.count

        }
#批次统计
class Picicount(BaseEntity):
    #批次
    picis = CharField(max_length=35)
    #数量
    count = CharField(max_length=35)

    class Meta:
        table_name = 'pici_count'

    def __str__(self):
        return self.picis

    def __dict__(self):
        return {
            'id': self.id,
            'picis': self.picis,
            'count': self.count

        }

#Schooldate 学校数据

class Schooldate(BaseEntity):
    #学校id
    schoolid = CharField(max_length=35)
    #学校名称
    name = CharField(max_length=35)
    #学校地址
    address = CharField(max_length=35)
    #学校简介
    info = CharField(max_length=35)
    #学校图片
    img = CharField(max_length=35)
    #学校分数
    score = CharField(max_length=35)
    #学校位次
    weici = CharField(max_length=35)
    #学校类型
    school_types = CharField(max_length=35)
    #学校批次
    school_pici = CharField(max_length=35)
    #学校类别
    school_leibie = CharField(max_length=35)

    class Meta:
        table_name = 'schooldate'

    def __str__(self):
        return self.name

    def __dict__(self):
        return {
            'id': self.id,
            'schoolid': self.schoolid,
            'name': self.name,
            'address': self.address,
            'info': self.info,
            'img': self.img,
            'score': self.score,
            'weici': self.weici,
            'school_types': self.school_types,
            'school_pici': self.school_pici,
            'school_leibie': self.school_leibie
        }


#scorecount 学校分数

class Scorecount(BaseEntity):

    #批次
    score = CharField(max_length=35)
    #数量
    count = CharField(max_length=35)

    class Meta:
        table_name = 'score_count'

    def __str__(self):
        return self.score

    def __dict__(self):
        return {
            'id': self.id,
            'score': self.score,
            'count': self.count

        }

#训练数据（xunlianshuju）
class Xunlianshuju(BaseEntity):
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

    like_school = CharField(max_length=35)
    wenke_school = CharField(max_length=35)
    chinese = CharField(max_length=35)
    math = CharField(max_length=35)
    english = CharField(max_length=35)
    physics = CharField(max_length=35)
    chemistry = CharField(max_length=35)
    biology = CharField(max_length=35)
    politics = CharField(max_length=35)
    history = CharField(max_length=35)
    geography = CharField(max_length=35)
    location = CharField(max_length=35)
    time = CharField(max_length=35)
    wenke_score = CharField(max_length=35)
    like_score = CharField(max_length=35)
    id = CharField(max_length=35)

    class Meta:
        table_name = 'xunlianshuju'

    def __str__(self):
        return self.id

    def __dict__(self):
        return {
            'id': self.id,
            'like_school': self.like_school,
            'wenke_school': self.wenke_school,
            'chinese': self.chinese,
            'math': self.math,
            'english': self.english,
            'physics': self.physics,
            'chemistry': self.chemistry,
            'biology': self.biology,
            'politics': self.politics,
            'history': self.history,
            'geography': self.geography,
            'location': self.location,
            'time': self.time,
            'wenke_score': self.wenke_score,
            'like_score': self.like_score
        }

#schoolinfoall 学校信息
class Schoolinfoall(BaseEntity):
    # schoolid
    # school_name
    # school_address
    # school_popularity
    # school_websit
    # jainjie
    # id
    schoolid = CharField(max_length=35)
    school_name = CharField(max_length=35)
    school_address = CharField(max_length=35)
    school_popularity = CharField(max_length=35)
    school_websit = CharField(max_length=35)
    jainjie = CharField(max_length=35)
    id = CharField(max_length=35)

    class Meta:#元数据
        table_name = 'schoolinfoall'

    def __str__(self):#返回字符串
        return self.id

    def __dict__(self):#返回字典
        return {
            'id': self.id,
            'schoolid': self.schoolid,
            'school_name': self.school_name,
            'school_address': self.school_address,
            'school_popularity': self.school_popularity,
            'school_websit': self.school_websit,
            'jainjie': self.jainjie
        }





