# -*- coding: utf-8 -*-#
#  @Time    :2019/3/4  
#  @Author  :jun
#  @Email   :1044622996@qq.com      
#  @File    : class_selenium.py
#  @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 去除 页面 Chrome 正受到自动测试软件的控制
# option = webdriver.ChromeOptions
# # option.add_argument("--disable-infobars")

# 打开谷歌浏览器

driver = webdriver.Chrome() # 打开浏览器
# 显示等待
# WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"kw")))
# 访问百度首页
# 隐形等待 设置一次，全局都可用 ，等待10s
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")   # 打开百度

WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH,'//a[@name="tj_settingicon" and @id = "s_usersetting_top"]'))).click()

# driver.find_element_by_xpath('//a[@name="tj_settingicon" and @id = "s_usersetting_top"]').click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH,'//a[text() = "高级搜索"]'))).click()

WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH,'//*[@id="adv-setting-5"]/select'))).click()

# sele = Select(e):
# print(sele.options)

# 定位元素
# ele = driver.find_element_by_xpath('//input[@id = "kw"]') # xpath
# ele = driver.find_elements_by_id('kw')   # id
# ele = driver.find_element_by_name('s_ipt')
# print(ele.tag_name)
# print(ele.get_attribute("name"))  # 获取属性值
#
#
# ele.send_keys('aaa')  # 发送内容
#
# driver.find_element_by_id('su').click()  # 根据id定位 点击搜索

# # 清空输入框
# ele.clear()
#
# ele.send_keys('python自动化')
#
# driver.find_element_by_id('su').click()



# 元素定位
# 1. id
# ele = driver.find_element_by_id('kw')  # 定位元素
# print(ele)
# print(ele.get_attribute('class'))
#
# # 2. name+
# driver.find_element_by_class_name()  # class
# driver.find_element_by_tag_name() # 标签名(h1)
# driver.find_elements_by_link_text('新')   文本
# driver.find_elements_by_partial_link_text('新') # 超链接  部分包含
#
# driver.find_element_by_class_name()
# driver.find_element_by_css_selector('input#kw.s_stt')  # Css 表达式

# driver.refresh() # 刷新
# driver.maximize_window()  # 全屏
# driver.save_screenshot()  # 截屏保存

# # driver.set_window_size(500,700) # # 调整大小
# driver.get("http://www.sogou.com")
# driver.back()  # 前进
# driver.forward() # 后退
# print(driver.current_url) # 获取url2
# print(driver.title)
driver.close()  # 关闭标签
driver.quit() # 退出