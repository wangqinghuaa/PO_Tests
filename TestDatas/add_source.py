#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 22:20
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : add_source.py
# @Software : PyCharm


# 正常场景
succes = ("auto", "sdfsdfsdf")
add_name = ("大学语文", "大学语文课程", "5")


# 异常创建课程用例：
add_case = [{"addData.name":"大学语文", "addData.desc":"大学语文课程", "addData.display_idx":"5", "check":"错误 : 同名课程存在"}]