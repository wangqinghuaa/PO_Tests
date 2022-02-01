#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 15:50
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : home_page.py
# @Software : PyCharm


from PageLocators.home_page_locs import HomepageLocs as locs
from Common.basepage import BasePage


class HomePage(BasePage):

    # 是否存在状态:存在返回True,不存在返回False
    def get_element_exists(self):
        doc = "添加课程页面_获取退出按钮"
        try:
            self.wait_ele_visible(locs.exit_link, doc)
        except:
            return False
        else:
            return True

    def get_element_univ(self):
        doc = "查看添加课程界面是否有大学语文名称字段"
        try:
            self.wait_ele_visible(locs.univ_chinese, doc)

        except:
            return False
        else:
            return True