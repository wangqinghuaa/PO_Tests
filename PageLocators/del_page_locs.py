#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-29 20:17
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : del_page_locs.py
# @Software : PyCharm


from selenium.webdriver.common.by import By

class DelPageLocs():

    #删除课程
    del_course=(By.XPATH, '//span[text()="大学语文"]')
    del_button=(By.XPATH,'//span[text()="大学语文"]/../../td[4]/button[2]')
    del_conf=(By.XPATH,'//button[@class="btn btn-primary"]')