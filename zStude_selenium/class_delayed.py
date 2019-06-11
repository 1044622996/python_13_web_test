# -*- coding: utf-8 -*-#
#  @Time    :2019/3/9  
#  @Author  :jun
#  @Email   :1044622996@qq.com      
#  @File    : class_delayed.py
#  @Software: PyCharm
# 功能： 增加显示等待

from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# driver.implicitly_wait(10)  # 隐式等待 全局

driver.get('http://www.baidu.com')

# 显式等待
wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"kw"))) # 直到一个元素满足条件

ele = driver.find_element_by_xpath('//input[@id="kw"]')
ele.send_keys('柠檬班')
driver.find_element_by_xpath('//input[@id="su"]').click() # 点击搜索


# 显式等待
m = WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH,'//a[contains(text(),"lemon.ke.qq.com")]'))) # 直到一个元素满足条件

# m = driver.find_element_by_xpath('//a[contains(text(),"lemon.ke.qq.com")]')
m.click()

# 切换页面
# WebDriverWait(driver,20).until(EC.new_window_is_opened(driver.current_window_handle))
windows = driver.window_handles  # 获取页面数

# print(windows)
# print(driver.current_window_handle)  # 获取当前窗口

driver.switch_to.window(windows[-1])  # 获取最新的页面



# 显式等待
huahua = WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH,'//h4[text() ="华华老师"]')))  # 直到一个元素满足条件

print(huahua.tag_name)
print(huahua.text)

# import time
# time.sleep(10)  # 强制等待
driver.close()
driver.quit()
