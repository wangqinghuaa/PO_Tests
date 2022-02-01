#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-31 20:39
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : conftest.py.py
# @Software : PyCharm

import pytest
from selenium import webdriver
from TestDatas import Global_Datas as GD
from PageObjects.login_page import LoginPage

@pytest.fixture
def init_driver():
    '''
    前置：打开浏览器：访问系统网址
    后置： 退出浏览器
    :return:
    '''
    driver = webdriver.Chrome()
    driver.get(GD.login_url)
    yield driver
    driver.quit()


@pytest.fixture
def init_login(init_driver):
       '''
       执行顺序： init_driver的前置--init_login的前置--init_login的后置--init_driver后置
       :param init_driver:
       :return:
       '''
       LoginPage(init_driver).login(GD.user,GD.pwd)
       yield init_driver