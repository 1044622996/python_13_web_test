#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/3/12 16:20
# @Author: jun
# @FILe  : class_alert.py
# @Function:


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.implicitly_wait(10)  # 隐式等待 全局

driver.get('http://localhost:63342/python_13_web_test/login_html.html?_ijt=72u3mtbfvqu8fo5n0fv6p5ub3b')

alert = driver.switch_to.alert()
print(alert.text)
alert.accept() # 确认
alert.dismiss() # 取消

# 等待
WebDriverWait(driver, 20,1).until(EC.alert_is_present())
