#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/3/28 11:10
# @Author: jun
# @FILe  : My_config.py
# @Function: 配置类

from configparser import ConfigParser
from Common.file_path import File_Path

class ReadConf:

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(filenames = File_Path().conf_path(), encoding='UTF-8')

    def get_value(self, section, option):
        return self.cf.get(section,option)

    def get_int(self, section, option):
        return self.cf.get(section, option)

    def get_float(self, section, option):
        return self.cf.get(section, option)

    def get_boolean(self, section, option):
        return self.cf.get(section, option)

if __name__ == '__main__':
     res = ReadConf().get_value('log','col_level')
     print(res)