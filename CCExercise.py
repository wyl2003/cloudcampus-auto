#cloudcampus自动完成练习
#核心代码来自https://www.toralen.com/2022/06/07/webdriver-x-python-cloudcampous%e8%87%aa%e5%8a%a8%e5%88%b7%e4%bb%bb%e5%8a%a1%e8%84%9a%e6%9c%ac/
"""
@Description: CCExercise.py 配合url.txt使用
@Author: wyl2003
@Date: 2022-12-14 20:52:45
"""

#qs-startbutton h5p-joubelui-button h5p-button
from selenium import webdriver
import xlwt
from selenium.webdriver.common.by import By
import time

print("此脚本只是自动提交所有练习来解决问题，开发者不对任何使用造成的后果负责。注意url列表可能不适用于其他环境")
idname=input("输入账号：")
password=input("输入密码：")
workbook = xlwt.Workbook(encoding = 'utf-8')
url_txt = open('url.txt','r')
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
        iframe=driver.find_element(By.CLASS_NAME,"h5p-player.w-100.border-0")
        driver.switch_to.frame(iframe)
        iframe1=driver.find_element(By.CLASS_NAME,"h5p-iframe.h5p-initialized")
        driver.switch_to.frame(iframe1)
        leixing=0
        try:
            quiz = driver.find_element(By.CLASS_NAME,"qs-startbutton.h5p-joubelui-button.h5p-button")
        except:
            leixing=1
        if leixing ==1:
            try:
                page = driver.find_element(By.CLASS_NAME,"progress-dot.unanswered")  # 存在翻页点
            except:
                leixing =2
        if leixing ==2:
            try:
                driver.find_element(By.CLASS_NAME,"h5p-question-check-answer.h5p-joubelui-button")
            except:
                leixing=4
        if leixing ==2:
            try:
                driver.find_element(By.CLASS_NAME,"h5p-question-next")
                leixing=3
            except:
                leixing=2
        if leixing==0:
            quiz = driver.find_element(By.CLASS_NAME,"qs-startbutton.h5p-joubelui-button.h5p-button")
            driver.execute_script("arguments[0].scrollIntoView();", quiz)
            quiz.click()
            nexts = driver.find_elements(By.CLASS_NAME,"h5p-question-next")
            a = driver.find_elements(By.CLASS_NAME,"h5p-question-check-answer.h5p-joubelui-button")
            for i in range(len(a)):
                driver.execute_script("arguments[0].scrollIntoView();", a[i])
                time.sleep(3)
                a[i].click()
                try:
                    nexts[i].click()
                except:
                    try:
                        time.sleep(3)
                        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.CLASS_NAME,"h5p-question-finish"))
                        driver.find_element(By.CLASS_NAME,"h5p-question-finish").click()
                    except:
                        print(url, "无finish按钮，需要做对几个")
        if leixing==1:
            nexts = driver.find_elements(By.CLASS_NAME,"h5p-question-next")
            a = driver.find_elements(By.CLASS_NAME,"h5p-question-check-answer.h5p-joubelui-button")
            for i in range(len(a)):
                driver.execute_script("arguments[0].scrollIntoView();", a[i])
                time.sleep(1)
                a[i].click()
                try:
                    nexts[i].click()
                except:
                    try:
                        time.sleep(1)
                        driver.execute_script("arguments[0].scrollIntoView();",
                                              driver.find_element(By.CLASS_NAME,"h5p-question-finish"))
                        driver.find_element(By.CLASS_NAME,"h5p-question-finish").click()
                    except:
                        print(url, "无finish按钮")
        if leixing==2:
            a = driver.find_elements(By.CLASS_NAME,"h5p-question-check-answer.h5p-joubelui-button")
            for i in a:
                driver.execute_script("arguments[0].scrollIntoView();", i)
                time.sleep(1)
                i.click()
        if leixing==3:
            nexts = driver.find_elements(By.CLASS_NAME,"h5p-question-next")
            a = driver.find_elements(By.CLASS_NAME,"h5p-question-check-answer.h5p-joubelui-button")
            for i in range(len(a)):
                driver.execute_script("arguments[0].scrollIntoView();", a[i])
                time.sleep(1)
                a[i].click()
                try:
                    nexts[i].click()
                except:
                    try:
                        time.sleep(1)
                        driver.execute_script("arguments[0].scrollIntoView();",
                                              driver.find_element(By.CLASS_NAME,"h5p-question-finish"))
                        driver.find_element(By.CLASS_NAME,"h5p-question-finish").click()
                    except:
                        print(url, "无finish按钮，需要做对几个")
        if leixing==4:
            print(url+"需要自己点")
    except:
        pass#如果出现卡住情况跳过
