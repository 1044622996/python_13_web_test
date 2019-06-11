# -*- coding: utf-8 -*-#
#  @Time    :2019/3/9  
#  @Author  :jun
#  @Email   :1044622996@qq.com      
#  @File    : calss_iframe.py
#  @Software: PyCharm
#  功能： iframe ,alert 定位

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)  # 隐式等待 全局

driver.get('https://www.ketangpai.com/User/login.html')

# 显式等待
wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//a[text()="微信登录"]'))).click()  # 点击搜索

# iframe 等待
ele = driver.find_elements_by_tag_name("iframe")
# driver.switch_to.frame(0)

# 定义iframe页面元素
WebDriverWait(driver,30).until(
    EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'iframe')))

wx = WebDriverWait(driver, 20,1).until(EC.element_to_be_clickable(
    (By.XPATH, '//div[@class ="title" ]')))

print(wx.text)

# # 退回到主页面
# driver.switch_to.default_content()
# # 退回到上一层
# driver.switch_to.parent_frame()



