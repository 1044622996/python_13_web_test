#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/2/27 14:29
# @Author: jun
# @FILe  : test.py
# @Function: selenium

# 测试内容：1.数据正常、2.UI 、交互
# 数据正常：1. 定位元素 doct['key']  2. DOM_OBJ.attr
# Document.getElementBy


from selenium import webdriver

# 打开谷歌浏览器
driver = webdriver.Chrome()
# 访问百度首页
driver.get("http://www.baidu.com")

# import requests
#
# url = 'http://localhost:63342/python_13_web_test/study_html.html?_ijt=iga66f8p0pu97k3qjj2gqsspn4'
# params = {
#     'command' : 'getElementById',
#     'iod':'title'
# }
# res = requests.get(url)
# print(res.text)
#
# def get_element_by_id(title):
#     params = {
#         'command': 'getElementById',
#         'iod': 'title'
#     }
#     requests.get(url,params)
#
# def get_element_by_name(title):
#     params = {
#         'command': 'getElementById',
#         'iod': 'title'
#     }
#     requests.get(url,params)
