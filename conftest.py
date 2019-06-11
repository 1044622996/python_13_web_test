#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/4/15 18:20
# @Author: jun
# @FILe  : conftest.py
# @Function:
import pytest
from selenium import webdriver
from Common.basepage import BasePage
from Pages.PageObjects.login_page import LoginPage
from Pages.PageObjects.bid_page import BidPage
from TestDatas.login_data import Login_data

@pytest.fixture(scope = 'class')  # 类中只实行一次 setUpclass
def init_driver():
    print("success start")
    driver = webdriver.Chrome()
    basepage = BasePage(driver)
    loginpage = LoginPage(driver)
    basepage.get_url()
    driver.maximize_window()
    yield (driver,loginpage)   # 相当于return,但可以继续执行后面的代码
    print("success end")

@pytest.fixture  # setUp
def my_set_class():  # 处理用例间互不影响
    print("begin start")

    yield   # 相当于return,但可以继续执行后面的代码

    print("qut end")

@pytest.fixture(scope = 'class')
def bid_driver():
    print("bid start")
    driver = webdriver.Chrome()
    basepage = BasePage(driver)
    loginpage = LoginPage(driver)
    basepage.get_url()
    bidpage  = BidPage(driver)
    driver.maximize_window()
    loginpage.submin_userinfo(Login_data.login_success['user'], Login_data.login_success['pwd'])

    yield (driver,bidpage) # 相当于return,但可以继续执行后面的代码
    print("bid end")

