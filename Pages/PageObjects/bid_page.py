#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/4/9 14:41
# @Author: jun
# @FILe  : bid_page.py
# @Function:投标
from selenium.webdriver.common.by import By
from Common.My_log import MyLog
from Common.basepage import BasePage

mylog = MyLog('投标')
class BidPage(BasePage):
    bid_ele = (By.XPATH,'//a[text()="抢投标"]') # 进行抢投标
    over = (By.XPATH, '//input[@data-amount]')  # 余额查看
    start_bid = (By.XPATH,'// button[text() = "投标"]') # 投标按钮
    bid_succ = (By.XPATH,'//div[text() = "投标成功！"]') # 投标成功，提示
    del_page = (By.XPATH,'//img[@src= "/Public/frontend/images/close_pop.png"]') # X按钮
    xiaomifeng = (By.XPATH,'//img[@class = "mr-5"]')  # 小蜜蜂
    Amount_Available = ('//li[@class = "color_sub"]')  # 可用金额
    Investment_project = (By.XPATH,'//div[@data-type = "tz"]')  # 投资项目
    money_integers = (By.XPATH,'//button[text() = "请输入10的整数倍"]')  # 10 的倍数
    bid_money_mi = (By.XPATH,'//div[@class="text-center"]')



    # 开始投标
    def bid(self):
        try:
            self.get_click_element(self.bid_ele)
            mylog.info('点击抢投标成功')
        except Exception as e:
            mylog.error('点击抢投标失败')
            self.save_screenshots()
            raise e

    # 金额框定位
    def get_bid(self):
        try:
            self.get_click_element(self.over)
            mylog.info('点击输入投标金额框成功')
        except Exception as e:
            mylog.error('点击输入投标金额框失败')
            raise e

    # 输入金额
    def input_bid_money(self,money):
        ele = self.wait_element(self.over)
        try:
            ele.send_keys(money)
            mylog.info('输入金额成功')
        except Exception as e:
            mylog.error('输入金额失败')
            self.save_screenshots()
            raise e

    def get_over(self):
        return self.get_bid().text

    # 点击投标
    def big_success(self):
        try:
            self.get_click_element(self.start_bid)
            mylog.info('点击投标成功')
        except Exception as e:
            mylog.error('点击投标失败')
            self.save_screenshots()
            raise e

    # 判断投标成功条件
    # 1. 弹出投标成功页面
    def big_success_tishi(self):
        return self.wait_element(self.bid_succ).text


    # 2. 可投标金额减少10000
    def get_bid_over(self):
        return  self.wait_element(self.over).text

    # 3. 可用金额减少10000  3349950.48元
    def get_amount_available(self):
        return  self.wait_element(self.Amount_Available).text

    # 4. 标的信息
    def investment_project(self):
        ele = self.wait_element(self.Investment_project)
        try:
            ele.click()
            mylog.info('显示投资项目信息')
        except Exception as e:
            mylog.info('显示投资项目信息失败')
            self.save_screenshots()
            raise e

    def fail_tishi(self):
        return  self.get_click_element(self.del_page)

    def money_integer(self):
        return self.wait_element(self.money_integers).text

    def bid_money_min(self):
        return self.wait_element(self.bid_money_mi).text

    def bid_clear(self):
        return  self.wait_element(self.over).clear()

