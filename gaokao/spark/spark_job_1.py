#分数在650以上，600-650，550-600，550以下的学校
# -*- coding: utf-8 -*-
import findspark
import numpy as np
from jieba import analyse
from pyspark import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import when

findspark.init()

hadoop_url = 'hdfs://127.0.0.1:9000/{dir}/{file}'

spark = SparkSession.builder.appName("job1").getOrCreate()
file = spark.read.csv(hadoop_url.format(dir='gaokao/dataset', file='date1.csv'), header=True)
#统计分数在650以上，600-650，550-600，500-550,400-500,400以下的学校（分数段）
file = file.withColumn('score', file['score'].cast('int'))
file = file.withColumn('score', when(file['score'] > 750, '650以上').otherwise(file['score']))
file = file.withColumn('score', when((file['score'] >= 650)& (file['score'] < 750), '650以上').otherwise(file['score']))
file = file.withColumn('score', when((file['score'] >= 600) & (file['score'] < 650), '600-650').otherwise(file['score']))
file = file.withColumn('score', when((file['score'] >= 550) & (file['score'] < 600), '550-600').otherwise(file['score']))
file = file.withColumn('score', when((file['score'] >= 500) & (file['score'] < 550), '500-550').otherwise(file['score']))
file = file.withColumn('score', when((file['score'] >= 400) & (file['score'] < 500), '400-500').otherwise(file['score']))
file = file.withColumn('score', when(file['score'] < 400, '400以下').otherwise(file['score']))
file = file.groupBy('score').count().orderBy('score')
file.show()

#写入hadoop
file.write.csv(hadoop_url.format(dir='gaokao/output', file='score_count.csv'), header=True, mode='overwrite')
spark.stop()



