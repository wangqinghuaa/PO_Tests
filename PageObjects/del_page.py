#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-29 20:16
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : del_page_locs.py
# @Software : PyCharm


# 所有浏览器都在这个类的继承下
from selenium.webdriver.remote.webdriver import WebDriver
from PageLocators.del_page_locs import DelPageLocs as dl

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DelPage:

    def __init__(self,driver:WebDriver): #: 声明这个引用的是 webdriver
        # 初始化 webdriver
        self.driver=driver

    # 删除课程
    def del_course(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(dl.del_course))
        time.sleep(2)
        self.driver.find_element(*dl.del_button).click()
        time.sleep(1)
        self.driver.find_element(*dl.del_conf).click()

