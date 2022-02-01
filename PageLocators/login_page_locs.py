#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 17:31
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : login_page_locs.py
# @Software : PyCharm


from selenium.webdriver.common.by import By

class LoginPageLocs():
    # 用户名输入框
    user_input = (By.XPATH, '//*[@id="username"]')
    # 密码输入框
    pass_input = (By.XPATH, '//*[@id="password"]')
    # 登录按钮
    login_button = (By.XPATH, '//*[@onclick="postLoginRequest()"]')

    # 获取登录错误的提示语
    msg_from_login_from = (By.XPATH, '//*[@class="modal-body"]//*[@class="bootstrap-dialog-message"]')



