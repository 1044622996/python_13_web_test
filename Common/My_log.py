#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/3/28 10:47
# @Author: jun
# @FILe  : My_log.py
# @Function: 日志类

import logging
from Common.file_path import File_Path
import logging.handlers
from Common.My_config import ReadConf

class MyLog:
    def __init__(self,log_name):
        self.log_name = log_name
        conf__path = ReadConf()  # 日志存储地址
        self.col_level = conf__path.get_value('log', 'col_level')  # 读取 日志收集器设置级别
        self.con_level = conf__path.get_value('log', 'con_level')  # 读取 输出到控制台设置级别
        self.log_lever = conf__path.get_value('log', 'log_lever')  # 读取 写入日志文件设置级别
        self.format = conf__path.get_value('log', 'format')        # 日志格式

    def mylog(self,level,msg):
        my_logger  = logging.getLogger(self.log_name)
        my_logger.setLevel(self.col_level)# 日志收集器设置级别
        format = logging.Formatter(self.format)

        # 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(self.con_level)
        ch.setFormatter(format)

        my_logger.addHandler(ch) # 收集器与控制台对接

        # 输出到日志文件
        fh = logging.handlers.RotatingFileHandler(File_Path().log_path(),maxBytes=20 *1024* 2014 ,backupCount=10, encoding='UTF-8') # 设置log文件
        fh.setLevel(self.log_lever)
        fh.setFormatter(format)

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level =='DEBUG':
            my_logger.debug(msg)

        elif level == 'INFO':
            my_logger.info(msg)

        elif level == 'WARNING':
            my_logger.warning(msg)

        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        # 如果出现重复日志，需加remove 对日志收集器进行移除
        my_logger.removeFilter(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.mylog('DEBUG',msg)

    def info(self,msg):
        self.mylog('INFO',msg)

    def warning(self, msg):
            self.mylog('WARNING', msg)

    def error(self,msg):
        self.mylog('ERROR',msg)


if __name__ == '__main__':
    my_log = MyLog('python13')
    my_log.error('我是debug')



