#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 14:45
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : login_page.py
# @Software : PyCharm


from PageLocators.login_page_locs import LoginPageLocs as locs
from Common.basepage import BasePage


class LoginPage(BasePage):

    # 登录操作-展示日志/截图/说明
    def login(self, username, password):
        self.input_text(locs.user_input, username, "登录页面_输入用户名")
        self.input_text(locs.pass_input, password,"登录页面_输入密码")
        self.click_element(locs.login_button, "登录页面_点击登录按钮")

    # 获取登录错误提示信息
    def get_error_msg(self):

        self.wait_ele_visible(locs.msg_from_login_from, "登录页面_获取登录区域的错误提示元素：")
        return self.get_ele_text(locs.msg_from_login_from, "登录页面_获取登录区域的错误提示元素：")



