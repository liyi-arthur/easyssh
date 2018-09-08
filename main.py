#!/usr/bin/env python
# encoding: utf-8
'''
@author: 
@license: (C) Copyright 2013-2025, MIT LICENSE
@contact: liyi_whu@163.com
@software: easyssh
@file: main.py
@time: 2018/9/8 21:18
@desc:
'''

import os
import sys
import getopt

def usage():
    print("Usage: %s [-a|-u|-p|-h]")

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:u:p:h")
        for opt, arg in opts:
            if opt in ("-a", ): pass
            elif opt in ("-u",): pass
            elif opt in ("-p",): pass
            elif opt in ("-h",): usage()
            else: usage()
    except getopt.GetoptError:
        usage()
