#!/usr/bin/env python
# encoding: utf-8
'''
@author: 
@license: (C) Copyright 2013-2025, MIT LICENSE
@contact: liyi_whu@163.com
@software: easyssh
@file: session.py
@time: 2018/9/8 22:53
@desc:
'''

class session(object):
    def __init__(self, ip="", user="", passwd=""):
        self.ip = ip
        self.user = user
        self.passwd = passwd

