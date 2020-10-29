# -*- coding: utf-8 -*-
# @Time     : 2020/10/24 8:03
# @Author   : chw
# @File     : break_continue.py

for i in range(1,10):
    if i == 6:
        # 此处使用break，等i为6时直接结束；此处使用continue，等i为6时直接执行i等于7的情况下
        continue
    print(i)