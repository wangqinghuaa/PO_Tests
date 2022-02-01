#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-29 23:34
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : dir_config.py.py
# @Software : PyCharm


import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir, "TestDatas")

testcases_dir = os.path.join(base_dir, "TestCases")


import time
now=time.strftime("%Y-%m-%d-%H:%M:%S")
htmlreport_dir = os.path.join(base_dir,r"Outputs\reports\reports.html")


logs_dir = os.path.join(base_dir, "Outputs\logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"Outputs\screenshots")


