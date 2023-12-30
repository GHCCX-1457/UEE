import requests
import csv

# 读取csv文件
with open('../finaldate/date1.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    urls= []
    ids = []
    for row in reader:
        # print(row)
        urls.append(row[4])
        ids.append(row[0])
    print(urls)
    urls.pop(0)
    #去掉第一个
    ids.pop(0)
    print(ids)

    for i in range(len(ids)):
        print(f"第{i}张图片开始下载")
        r = requests.get(urls[i])
        with open(f"../finaldate/img/{ids[i]}.jpg", "wb") as f:
            f.write(r.content)
        print(f"第{i}张图片下载完成")