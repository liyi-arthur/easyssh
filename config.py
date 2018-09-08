#!/usr/bin/env python
# encoding: utf-8
'''
@author: 
@license: (C) Copyright 2013-2025, MIT LICENSE
@contact: liyi_whu@163.com
@software: easyssh
@file: config.py.py
@time: 2018/9/8 22:59
@desc:
'''

import json
import session

config=None

def initconfig():
    with open(r"setting.json", "r", encoding="utf-8") as f:
        f.seek(0)
        global config
        config=json.load(f)
        #print(config)

def saveconfig():
    with open(r"setting.json", "w", encoding="utf-8") as f:
        f.seek(0)
        #print(json.dumps(config, indent=4))
        f.write(json.dumps(config, indent=4))

def insertSession(config, session):
    ss = config["sessions"]
    s = {}
    s["ip"] = session.ip
    s["user"] = session.user
    s["passwd"] = session.passwd
    ss.append(s)

if __name__ == '__main__':
    # global config
    initconfig()
    s = session.session("192.168.1.5", "root", "dddd")
    insertSession(config, s)
    saveconfig()