import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 调用键盘按键操作时需要引入的Keys包
import time
import re

import csv
with open('school_infoall.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 先写入columns_name
    writer.writerow(["id", "school_name", "school_address", "school_popularity", "school_websit","jainjie"])
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.Chrome("../evn/chromedriver.exe")
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
#读取csv
idList = []
with open('date1.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        idList.append(row[0])
#移除第一个元素
idList.pop(0)
print(idList)


for i in idList:
    try:
        driver.get("https://www.gaokao.cn/school/" + i)
        time.sleep(1)
        #采用class定位
        #名字
        school_name = driver.find_element(By.CLASS_NAME, 'line1-schoolName').text
        #地址
        school_address = driver.find_element(By.CLASS_NAME, 'line1-province').text
        #人气
        school_popularity = driver.find_element(By.CLASS_NAME, 'l-city').text
        #官网1
        school_websit= driver.find_element(By.CLASS_NAME, 'line3').text
        #简介
        jainjie = driver.find_element(By.CLASS_NAME, 'shcool-rank_introduceWrap__1mIL7').text

        dict = {}
        dict['school_name'] = school_name
        dict['school_address'] = school_address
        dict['school_popularity'] = school_popularity
        dict['school_websit'] = school_websit
        dict['jainjie'] = jainjie
        dict['id'] = i
        print(dict)
        # 写入csv文件
        with open('school_infoall.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # 先写入columns_name
            writer.writerow([dict['id'], dict['school_name'], dict['school_address'], dict['school_popularity'], dict['school_websit'],dict['jainjie']])
    except:
        print("出错了"+i)
        continue