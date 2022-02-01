#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 17:42
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : home_page_locs.py
# @Software : PyCharm

from selenium.webdriver.common.by import By

class HomepageLocs():
    exit_link = (By.XPATH, '//button[@ng-click="logout()"]')
    univ_chinese=(By.XPATH,'//span[text()="大学语文"]')