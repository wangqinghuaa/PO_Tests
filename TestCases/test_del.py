#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-29 20:11
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : test_del.py
# @Software : PyCharm

import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from PageObjects.del_page import DelPage
from TestDatas import Global_Datas as GD
from TestDatas import  login_datas as ld


class DelSource(unittest.TestCase):

    def setUp(self):
        # 访问首页-初始化webdriver
        self.driver=webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        pass
    def tearDown(self):
        self.driver.quit()

    def test_del_source(self):
        #1. 首页-获取元素是否存在
        LoginPage(self.driver).login(*ld.success)
        self.assertTrue(HomePage(self.driver).get_element_exists())
        DelPage(self.driver).del_course()


if __name__ == '__main__':
    unittest.main()