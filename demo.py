#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @FileName     :demo.py
# @Time         :2022/6/4 11:23
# @Author       :Henry Feng
# @Description  :

import uiautomator2 as u2

d = u2.connect()  # connect to device
print(d.info)
