#统计直辖市的学校数量
# -*- coding: utf-8 -*-
import findspark
import numpy as np
from jieba import analyse
from pyspark import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import when

findspark.init()

hadoop_url = 'hdfs://127.0.0.1:9000/{dir}/{file}'

spark = SparkSession.builder.appName("job2").getOrCreate()
file = spark.read.csv(hadoop_url.format(dir='gaokao/dataset', file='date1.csv'), header=True)
#
#模糊查询,统计直辖市的学校数量（字段为address）
beijing = file.filter(file['address'].like('%北京%')).count()
chongqing = file.filter(file['address'].like('%重庆%')).count()
shanghai = file.filter(file['address'].like('%上海%')).count()
tianjin = file.filter(file['address'].like('%天津%')).count()
print('北京的学校数量为：',beijing)
print('重庆的学校数量为：',chongqing)
print('上海的学校数量为：',shanghai)
print('天津的学校数量为：',tianjin)
dict_1 = {}

dict_1['beijing'] = beijing
dict_1['chongqing'] = chongqing
dict_1['shanghai'] = shanghai
dict_1['tianjin'] = tianjin
print(dict_1)

#将dict_1写入hadoop
dict_1 = spark.sparkContext.parallelize(dict_1.items())
dict_1 = dict_1.map(lambda x: Row(address=x[0], count=x[1]))
dict_1 = spark.createDataFrame(dict_1)
dict_1.show()
dict_1.write.csv(hadoop_url.format(dir='gaokao/output', file='city_count.csv'), header=True, mode='overwrite')
spark.stop()







