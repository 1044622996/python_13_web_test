#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/4/10 21:41
# @Author: jun
# @FILe  : test_bid.py
# @Function: 投资

import unittest
import pytest
from selenium import webdriver
from Pages.PageObjects.login_page import LoginPage
from TestDatas.login_data import Login_data
from ddt import ddt
from Common.My_log import MyLog
from TestDatas.bid_data import BidData
from Pages.PageObjects.bid_page import BidPage
from Common.basepage import BasePage


mylog = MyLog('投资日志')

@pytest.mark.all1
# @ddt
class TestBid:

    @pytest.mark.usefixtures('bid_driver')
    @pytest.mark.smoke
    def test_bid_success(self, bid_driver):
        driver, bidpage = bid_driver  # 进入投标页面
        bidpage.bid()
        #  输入金额
        bidpage.input_bid_money(BidData.bid_data["money"])
        # 点击投资
        bidpage.big_success()
        # 断言
        # self.assertTrue(self.bidpage.big_success_tishi(),BidData.bid_data["prompt"])
        assert bidpage.big_success_tishi(), BidData.bid_data["prompt"]
        bidpage.fail_tishi()
        # self.assertTrue(self.get_amount_available + BidData.bid_data["money"] == self.bidpage.get_bid())
        # assert self.get_amount_available + BidData.bid_data["money"], bidpage.get_bid()

    # 输入非10 倍数
    @pytest.mark.bid_fail_1
    def test_bid_fail_1(self, bid_driver):
        driver, bidpage = bid_driver
        # 进入投标页面
        bidpage.bid()
        #  输入金额
        bidpage.input_bid_money(BidData.bid_fail_1["money"])
        # 断言
        # assertTrue(self.bidpage.money_integer() == BidData.bid_fail_1["prompt"])
        assert bidpage.money_integer(), BidData.bid_fail_1["prompt"]


    @pytest.mark.bid_fail_2
    def test_bid_fail_2(self, bid_driver):
        driver, bidpage = bid_driver
        # 进入投标页面
        bidpage.bid()
        #  输入金额
        bidpage.input_bid_money(BidData.bid_fail_2["money"])
        # 点击投标
        bidpage.big_success()
        # 断言
        # self.assertTrue(self.bidpage.bid_money_min() == BidData.bid_fail_2["prompt"])
        assert bidpage.bid_money_min(), BidData.bid_fail_2["prompt"]


if __name__ == '__main__':
    unittest.main()
