import os

# 执行命令hadoop fs -ls / 查看是否创建成功

hadoop_url = 'hdfs://127.0.0.1:9000/{dir}/{file}'
hadoop_upload_command = 'hadoop fs -put {local_path} {hadoop_path}'


def upload_file_to_hadoop(local_path, hadoop_path):
    os.system(hadoop_upload_command.format(local_path=local_path, hadoop_path=hadoop_path))


def loadFileList(dir):
    return os.listdir(dir)


commands = [
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/gaokao',
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/gaokao/dataset',
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/gaokao/output',

]

# 创建文件夹
for command in commands:
    print(f'执行命令：{command}')
    os.system(command)

# 上传文件到hadoop
print('正在上传文件：date1.csv')
upload_file_to_hadoop('dataset/date1.csv',
                      hadoop_url.format(dir='gaokao/dataset', file='date1.csv'))

