#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 21:54
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : add_page.py
# @Software : PyCharm


from PageLocators.add_page_locs import AddPageLocs as locs
from Common.basepage import BasePage


class AddPage(BasePage):

    # 添加课程
    def add_course(self, course_name, depict_name, sp_name):
        self.click_element(locs.add_course, "登录页面_点击添加课程")
        self.input_text(locs.course_name, course_name, "输入课程名称")
        self.input_text(locs.depict_name, depict_name, "输入课程名称描述")
        self.input_text(locs.sp_name, sp_name, "输入课程展示次序")
        self.click_element(locs.add_button, "点击创建")
        # self.click_element(locs.cancel_button, "点击取消按钮")

    # 获取添加课程错误提示信息
    def get_error_msg(self):

        self.wait_ele_visible(locs.msg_from_add_from, "添加课程页面_获取添加课程的错误提示：")
        return self.get_ele_text(locs.msg_from_add_from, "添加课程页面_获取添加课程的错误提示：")
