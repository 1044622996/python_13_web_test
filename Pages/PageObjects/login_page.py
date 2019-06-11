#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/3/20 21:56
# @Author: jun
# @FILe  : login_page.py
# @Function:

from selenium.webdriver.common.by import By
from Common.basepage import BasePage


class LoginPage(BasePage):

    phone = (By.NAME,'phone')
    passwd = (By.NAME,'password')
    login_ture = (By.XPATH,'//img[@class= "mr-5"]')  # 小蜜蜂
    errouser_null = (By.XPATH,'//div[@class="form-error-info"]')
    alert_tishi = (By.XPATH,'// div[@class ="layui-layer-content"]')
    loginBetton = (By.XPATH, '//a[text() = "登录"]')
    user_quit = (By.XPATH,'//a[text() = "退出"]')

    def submin_userinfo(self,user,pwd):  # 登录信息
        self.get_phone_element().send_keys(user)
        self.get_pwd_element().send_keys(pwd)
        self.get_phone_element().submit()

    def login_quit(self):
        return self.get_click_element(self.user_quit)

    def login_betton(self):   # 进入登录页面
        return self.get_click_element(self.loginBetton)

    def get_phone_element(self):  # 用户账号
        return self.wait_element(self.phone)

    def get_pwd_element(self):  # 用户密码
        return self.wait_element(self.passwd)

    def clear_phone(self):       # 清除账号
        return self.get_phone_element().clear()

    def clear_pwd(self):         # 清除密码
        return self.get_pwd_element().clear()

    def get_tishi(self):
        return self.wait_element(self.errouser_null)

    def login(self):   # 登录验证
        return self.wait_element(self.login_ture)

    def alert_element(self):
        return self.wait_element(self.alert_tishi)


