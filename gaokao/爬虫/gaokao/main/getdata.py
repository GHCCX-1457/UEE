import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 调用键盘按键操作时需要引入的Keys包
import time
import re

import csv

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.Chrome("../evn/chromedriver.exe")
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("https://www.gaokao.cn/lineschool")
flask = 1
# 创建csv文件
with open('school.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 先写入columns_name
    writer.writerow(["id", "name", "address", "info", "img"])

# 获取大学
for j in range(0, 78):
    print(f"第{j + 1}页开始")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    school_names = driver.find_elements(By.XPATH,
                                        '//*[@id="root"]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/h3/em')
    school_address = driver.find_elements(By.XPATH,
                                          '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/div/div[2]/div[1]/h3/span')
    school_infos = driver.find_elements(By.XPATH,
                                        '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]')

    # 学校图片
    school_imgs = driver.find_elements(By.XPATH,
                                       '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/img')

    schools = []

    for i in range(len(school_names)):
        school = {}
        school['name'] = school_names[i].text
        school['address'] = school_address[i].text
        school['info'] = school_infos[i].text
        school['img'] = school_imgs[i].get_attribute('src')
        school['id'] = re.findall(r"\d+\.?\d*", school['img'])[0]
        # 去掉小数点
        school['id'] = school['id'].replace('.', '')
        schools.append(school)

        # 写入csv文件

        with open('school.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # 先写入columns_name
            writer.writerow([school['id'], school['name'], school['address'], school['info'], school['img']])

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"第{j + 1}页完成")

    # 点击下一页
    if j < 3 or j>74:
        next_page = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/div/ul/li[9]/span')
    elif j == 3 or j == 74:
        next_page = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/div/ul/li[10]/span')
    elif 74 > j > 4:
        next_page = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/div/ul/li[11]/span')
    next_page.click()
    if flask == 1:
        time.sleep(30)
        flask = 0
        next_page = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/div/ul/li[9]/span')
        next_page.click()
print("《《《《《《《《《《《《《《《《《《《《《《《《《《《《《《《《")
print("全部完成")
