#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/3/28 15:26
# @Author: jun
# @FILe  : file_path.py
# @Function:

import os
import time


class File_Path:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.dirname(__file__))
        self.time= time.strftime('%Y-%m-%d')
        self.time2 = time.strftime('%Y-%m-%d %H:%M:%S')
    def conf_path(self):
        return os.path.join(self.dir_path,'Config','case.Config')

    def log_path(self):
        return os.path.join(self.dir_path, 'Outputs\logs',self.time +'.log')

    def report_path(self):
        report_path = os.path.join('test_report_'+ self.time + '.html')
        return  os.path.join(self.dir_path,'Outputs\Reports',report_path)

    def err_photo(self):
        return os.path.join(self.dir_path, 'Outputs\screenshots', self.time2 + '.jpg')

    def test_path(self):
        return os.path.join(self.dir_path,'TestCases')

if __name__ == '__main__':
    print('配置地址:', File_Path().conf_path())
    print('日志地址:', File_Path().log_path())
    print('报告地址:', File_Path().report_path())
    print('测试用力地址',File_Path().test_path())
    print(File_Path().err_photo())
