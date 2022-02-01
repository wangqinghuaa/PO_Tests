#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 21:49
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : add_page.py.py
# @Software : PyCharm

# 添加课程

import time

from PageObjects.home_page import HomePage
from PageObjects.add_page import AddPage
from TestDatas import add_source as ass
import logging
import pytest


@pytest.mark.usefixtures("init_login")
class TestAdd:

    def test_add_success(self, init_login):
        assert HomePage(init_login).get_element_exists()
        logging.info("***添加课程用例_正常添加课程***")
        AddPage(init_login).add_course(*ass.add_name)
        assert HomePage(init_login).get_element_univ()

    @pytest.mark.parametrize("case", ass.add_case)
    def test_add_tailed_no_username(self, case, init_login): # 注意顺序执行
        # 步骤:添加相同的课程
        assert HomePage(init_login).get_element_exists()
        lp = AddPage(init_login)
        logging.info("***添加课程用例：异常场景/添加相同的课程")
        lp.add_course(case["addData.name"], case["addData.desc"], case["addData.display_idx"])
        assert lp.get_error_msg(), case["check"]
        time.sleep(1)

    # def test_add_vdelete(self):  #删除课程
    #     LoginPage(self.driver).login(*ld.success)
    #     self.assertTrue(HomePage(self.driver).get_element_exists())


