# -*- coding: utf-8 -*-
# @Time     : 2020/10/24 8:07
# @Author   : chw
# @File     : guess_num.py
import random

computer_num = random.randint(1,101)
# print(computer_num)
while True:
    person_num = int(input("please input your num:"))
    if person_num > computer_num:
        print("小一点")
    elif person_num < computer_num:
        print("大一点")
    else:
        print("猜对了")
        break