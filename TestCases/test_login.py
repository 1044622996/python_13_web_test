#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/3/20 20:42
# @Author: jun
# @FILe  : test_login.py
# @Function: 登录

import unittest
import pytest
from selenium import webdriver
from Pages.PageObjects.login_page import LoginPage
from TestDatas.login_data import Login_data
from ddt import ddt,data
from Common.My_log import MyLog
from Common.basepage import BasePage

mylog = MyLog('登录日志')

# @ddt
@pytest.mark.all
class TestLogin:
    @pytest.mark.usefixtures('init_driver')
    @pytest.mark.smoke
    # @data(*Login_data.login_fail)
    @pytest.mark.parametrize('logindata',Login_data.login_fail)
    def test_login_fail(self,logindata,init_driver):
        driver,loginpage = init_driver
        loginpage.clear_phone()
        loginpage.clear_pwd()
        loginpage.submin_userinfo(logindata['user'],logindata['pwd'])
        try:
            # self.assertTrue(logindata['tip'] ,self.loginpage.get_tishi())
            assert  logindata['tip'] ,loginpage.get_tishi()
            mylog.info('提示显示正确')
        except Exception as e:
            mylog.error('提示显示错误')
            raise e

    @pytest.mark.login_1
    def test_login_popup(self,init_driver):
        driver, loginpage = init_driver
        loginpage.clear_phone()
        loginpage.clear_pwd()
        loginpage.submin_userinfo(Login_data.login_Popup['user'],Login_data.login_Popup['pwd'])
        try:
            # self.assertTrue(Login_data.login_Popup['tip'],self.loginpage.alert_element())
            assert Login_data.login_Popup['tip'] ,loginpage.alert_element()
        except Exception as e:
            mylog.error('提示显示错误')
            raise e

    @pytest.mark.login_2
    def test_login_success(self, init_driver):
        driver, loginpage = init_driver
        loginpage.submin_userinfo(Login_data.login_success['user'], Login_data.login_success['pwd'])
        try:
            # self.assertTrue(Login_data.login_success['tip'], self.loginpage.login())
            assert Login_data.login_success['tip'],loginpage.login()
            mylog.info('登录成功')
        except Exception as e:
            mylog.error('登录失败')
            raise e

if __name__ == '__main__':
    TestLogin()
