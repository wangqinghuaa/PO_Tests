#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-28 22:05
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : add_page_locs.py
# @Software : PyCharm


from selenium.webdriver.common.by import By

class AddPageLocs():

    #添加课程
    add_course=(By.XPATH, '//button[@ng-click="showAddOne=true"]')
    course_name=(By.XPATH, '//input[@ng-model="addData.name"]')
    depict_name=(By.XPATH, '//textarea[@ng-model="addData.desc"]')
    sp_name=(By.XPATH, '//input[@ng-model="addData.display_idx"]')
    add_button=(By.XPATH, '//button[@ng-click="addOne()"]')

    # cancel_button=(By.XPATH, '//button[@ng-click="$parent.showAddOne=false"]') # 点击取消

    #获取添加课程错误的提示语
    msg_from_add_from = (By.XPATH, '//*[@class="bootstrap-dialog-body"]/*[@class="bootstrap-dialog-message"]')



