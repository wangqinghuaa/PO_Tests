#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 14:40
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : test_login.py
# @Software : PyCharm


from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from TestDatas import login_datas as ld
import logging
import pytest


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.smoke
    def test_login_success(self,init_driver):
        # 步骤:登录页面-登录操作
        logging.info("***登录用例_正常场景-登录成功***")
        LoginPage(init_driver).login(*ld.success)
        assert HomePage(init_driver).get_element_exists()


    @pytest.mark.parametrize("case",ld.case)
    def test_login_tailed_no_username(self, case, init_driver):  # 注意顺序执行
        # 步骤:登录页面-登录操作
        logging.info("***登录用例：异常场景-登录失败")
        lp = LoginPage(init_driver)
        lp.login(case["username"], case["password"])
        # 断言
        assert lp.get_error_msg(), case["check"]





