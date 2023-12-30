import findspark
from pyspark.sql import SparkSession

findspark.init()

hadoop_url = 'hdfs://127.0.0.1:9000/{dir}/{file}'
spark = SparkSession.builder.appName("download").getOrCreate()


def download(file_name):
    print(f'正在下载文件：{file_name}')
    # 将处理好的数据下载到本地,并保存到output目录下
    df = spark.read.csv(
        hadoop_url.format(dir='gaokao/output/', file=file_name),
        header=True, encoding='utf-8', emptyValue='', mode='DROPMALFORMED', sep=','
    )
    df.toPandas().to_csv(f'output/{file_name}.csv', encoding='utf-8', index=False)

download('score_count.csv')
download('city_count.csv')