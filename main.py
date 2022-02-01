#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-02-01 21:57
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : main.py
# @Software : PyCharm


import pytest

# 使用html报告
# pytest.main(["-s","-v","-m","smoke","--html=Outputs/report.html","--reruns","2","--reruns-delay","5"])

# 使用allure报告生成
# pytest.main(["-s","-v","--html=Outputs/reports/pytest.html",
#                   "--alluredir=Outputs/allure"])

# pytest.main(["-s","-v","--alluredir=Outputs/allure"])

# pytest.main(["--reruns", "2", "--reruns-delay", "5", "-s", "-v", "--junitxml=Outputs/reports/report.xml",
#               "--html=Outputs/reports/html_report.html", "--alluredir=Outputs/allure_reports"])

pytest.main(["--reruns", "2", "--reruns-delay", "5", "-s", "-v", "--alluredir = Outputs/allure_reports"])
