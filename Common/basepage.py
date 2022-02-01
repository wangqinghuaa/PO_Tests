#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-29 22:28
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : basepage.py
# @Software : PyCharm


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.dir_config import screenshot_dir
from Common import logger

import logging
import time
import datetime

# 记录日志、失败截图、错误信息输出、抛出异常

class BasePage:

    def __init__(self, driver: WebDriver):

        self.driver = driver

    # 等待可见
    def wait_ele_visible(self,loc,img_name,timeout=20,poll_fre=0.5):
        logging.info("{}等待{}元素可见".format(img_name,loc))
        try:
            start_time = datetime.datetime.now() # 等待开始时间，引入datetime
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
            end_time = datetime.datetime.now() # 等待结束时间
            logging.info("开始等待时间：{}，结束等待时间：{}，等待时长为：{}".format(start_time, end_time, end_time - start_time))
        except:
            self.save_page_shot(img_name)
            logging.exception("等待元素可见失败：")
            raise

    # 等待元素可点击(拓展)
    def wait_ele_clickable(self,loc,img_name,timeout=20,poll_fre=0.5):
        try:
            start_time = datetime.datetime.now() # 等待开始时间，引入datetime
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(EC.element_to_be_clickable(loc))
            end_time = datetime.datetime.now() # 等待结束时间
            logging.info("开始等待时间：{}，结束等待时间：{}，等待时长为：{}".format(start_time, end_time, end_time - start_time))
        except:
            self.save_page_shot(img_name)
            logging.exception("等待元素可见失败：")
            raise



    # 查找元素
    def get_element(self, loc, img_name):
        logging.info("在{}查找元素：{}".format(img_name, loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            logging.exception("查找元素失败")
            self.save_page_shot(img_name)
            raise
        else:
            return ele

    # 点击元素
    def click_element(self, loc,img_name, timeout=30,poll_fre=0.5):
        logging.info("在{}点击{}元素".format(img_name, loc))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)  # 必然的前提
        ele = self.get_element(loc, img_name)    # 必然的前提
        try:
            ele.click()  # 点击操作
        except:
            logging.exception("点击元素失败")
            self.save_page_shot(img_name)
            raise
        else:
            return ele

    # 元素输入操作
    def input_text(self, loc, value, img_name, timeout=20,poll_fre=0.5):
        logging.info(" 在{}往元素 {} 输入文本值:{}".format(img_name, loc, value))
        self.wait_ele_visible(loc, img_name,timeout,poll_fre)  # 必然的前提
        ele = self.get_element(loc,img_name)    # 必然的前提
        try:
            ele.send_keys(value)
        except:
            self.save_page_shot(img_name)
            logging.exception("元素输入文本失败")
            raise

    # 获取元素属性
    def get_ele_attribute(self,loc,attr_name,img_name,timeout=20,poll_fre=0.5):
        logging.info("在{}获取元素 {} 的{}属性".format(img_name, loc, attr_name))
        self.wait_ele_visible(loc,img_name,timeout,poll_fre)  # 必然的前提
        ele = self.get_element(loc,img_name)    # 必然的前提
        try:
            value = ele.get_attribute(attr_name)
        except:
            # 日志
            logging.exception("获取元素属性失败!")
            # 截图
            self.save_page_shot(img_name)
            raise
        else:
            logging.exception("属性值为：{}".format(value))
            return value

    # 获取元素的文本值
    def get_ele_text(self, loc, img_name, timeout=20,poll_fre=0.5):
        logging.info("在{}获取元素的文本内容 {}".format(img_name, loc))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)  # 必然的前提
        ele = self.get_element(loc, img_name)  # 必然的前提
        try:
            text = ele.text
        except:
            logging.exception("获取元素文本失败!")
            self.save_page_shot(img_name)
            raise
        else:
            logging.exception("文本值为：{}".format(text))
            return text

    # 获取截图
    def save_page_shot(self, img_name):
        '''
        :param filepath:
        :param img_name:页面名称_页面行为
        :return:
        '''

        # 将图片储存在Outputs.screenshots下面，唯一不同-图片命名
        # 命名规范-{页面名称_页面行为}_时间_png
        # 文件完整名称：Outputs.screenshots+{页面名称_页面行为}_时间_png
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        file_path= screenshot_dir+"/{}_{}.png".format(img_name,now)
        try:
            self.driver.save_screenshot(file_path)
            logging.info("截取当前网页成功并储存在：{}".format(file_path))
        except:
            logging.exception("网页截屏失败！")
            raise

    # 切换到新的窗口
    # iframe切换
    # js执行
    # 滚动条操作
    # 上传操作


    #iframe切换
    # def swith_to_iframe(self,loc):
    #     try:
    #         iframe = WebDriverWait(self,driver,20).until(EC.frame_to_be_available_and_switch_to_it(loc))
    #         return iframe
    #     except:
    #         logging.exception("iframe切换失败")




if __name__ == '__main__':
    # from selenium import webdriver
    # driver=webdriver.Chrome()
    # driver.get("http://www.baidu.com")
    # bp=BasePage(driver)
    # # search_loc=("id","kw")
    # # bp.input_text(search_loc,"柠檬班","百度页面_搜索输入操作")
    pass
    # from selenium import webdriver
    # driver=webdriver.Chrome()
    # driver.get("https://music.163.com/#/discover/toplist")
    # bp=BasePage(driver)
    # iframe=("g_iframe")
    # bp.swith_to_iframe(iframe)
