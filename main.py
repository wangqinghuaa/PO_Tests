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


# 使用allure生成的报告
# pytest.main(["--reruns", "2", "--reruns-delay", "5", "-s", "-v", "--junitxml=Outputs/reports/report.xml",
#               "--html=Outputs/reports/html_report.html", "--alluredir=Outputs/allure_reports"])

# 使用allure生成的报告(优先)
# pytest.main(["-s", "-v", "--html=Outputs/reports/pytest.html", "--alluredir=Outputs/allure"])

pytest.main(["-s", "-v", "-m", "regress",
             "--reruns", "2", "--reruns-delay", "5","--alluredir=Outputs/allure",
             "--html=Outputs/reports/reports.html"])

