#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/4/9 10:35
# @Author: jun
# @FILe  : basepage.py
# @Function:

# from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Common.file_path import File_Path
from Common.My_log import MyLog

mylog = MyLog('登录')

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    # 延时等待 元素可见
    def wait_element(self,locator,timeout =20):
        try:
            return  WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        except Exception as e:
            mylog.error('延时等待超时')
            raise e

    # 元素点击
    def get_click_element(self,locator):
        ele = self.wait_element(locator)
        try:
            ele.click()
        except Exception as e:
            mylog.error('点击元素失败')
            raise e

    def save_screenshots(self):
        filepath = File_Path().err_photo()
        try:
            self.driver.save.screenshots(filepath)
            mylog.info('截图所在路径：{}'.format(filepath))
        except Exception as e :
            mylog.error('截图失败')
            raise e
    def get_url(self):
        url = 'http://120.78.128.25:8765/Index/login.html'
        self.driver.get(url)


    def seitch_window(self,name = None):  # 切换页面
        if name is None:
            current_handle = self.driver.current_window_handle
            WebDriverWait(self.driver,20).until(ec.new_window_is_opened(current_handle))
            handles = self.driver.window_handles             # 获取当前窗口
            return self.driver.switch_to.window(handles[-1])   # 获取新页面
        return  self.driver.switch_to.window(name)