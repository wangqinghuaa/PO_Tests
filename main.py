#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-02-01 21:57
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : main.py
# @Software : PyCharm

from Common import dir_config
import pytest


pytest.main(["-s","-v","-m","smoke","--html={0}".format(dir_config.htmlreport_dir)])


