#cloudcampus自动完成文件
#核心代码来自https://www.toralen.com/2022/06/07/webdriver-x-python-cloudcampous%e8%87%aa%e5%8a%a8%e5%88%b7%e4%bb%bb%e5%8a%a1%e8%84%9a%e6%9c%ac/
"""
@Description: CCExercise.py 配合furl.txt使用
@Author: wyl2003
@Date: 2022-12-14 20:52:45
"""

from selenium import webdriver
import xlwt
from selenium.webdriver.common.by import By
import time

print("此脚本只是自动点击所有文件来解决问题，开发者不对任何使用造成的后果负责。注意furl列表需要自行更新")
idname=input("输入账号：")
password=input("输入密码：")
workbook = xlwt.Workbook(encoding = 'utf-8')
url_txt = open('furl.txt','r')
url_list = url_txt.read().split('\n')
driver = webdriver.Chrome()
time.sleep(8)
driver.get("https://www.cloudcampus.com.cn/")
time.sleep(9)
driver.find_element(By.ID,'username').send_keys(idname)
driver.find_element(By.ID,'password').send_keys(password)
driver.find_element(By.ID,"loginbtn").click()
for url in url_list:
    try:
        driver.get(url)
        time.sleep(7)
        done = driver.find_element(By.CLASS_NAME,"btn.btn-outline-secondary.btn-sm.text-nowrap")
        done.click()
        time.sleep(3.5)
    except:
        pass
