#!/usr/bin/bin python
# -*- coding: utf-8 -*-
# @Time  : 2019/4/15 17:41
# @Author: jun
# @FILe  : pytest_report.py
# @Function:

import pytest



if __name__ == '__main__':
    pytest.main(['-m smoke',
                 '--capture=no'
                 ])

