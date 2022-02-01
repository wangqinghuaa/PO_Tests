#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 20:02
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : login_datas.py
# @Software : PyCharm


#正常场景
success = ("auto", "sdfsdfsdf")


#异常登录用例：密码错误/空用户名/空密码
case=[{"username":"auto","password":"sdfsdfs","check":"登录失败 : 用户或者密码错误"},
       {"username": "", "password": "sdfsdfsdf", "check": "登录失败 : 用户或者密码错误"},
       {"username": "auto", "password": "", "check": "登录失败 : 用户或者密码错误"},]