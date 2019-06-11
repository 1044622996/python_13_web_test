#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/4/15 14:27
# @Author: jun
# @FILe  : Main.py
# @Function:

# import unittest
# from Common.file_path import File_Path
# import HTMLTestRunnerNew
#
# test_path = File_Path().test_path()
# discore = unittest.defaultTestLoader.discover(test_path,pattern="test_*.py",top_level_dir=test_path)
#
# report_path = File_Path().report_path()
# with open(report_path,'wb') as file:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='前程贷登录，投资测试报告',description=None,tester='jun')
#     runner.run(discore)

import pytest

if __name__ == '__main__':
    pytest.main(['-m all','--capture=no', '--alluredir=Outputs/allure'])