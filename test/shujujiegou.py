# -*- coding: utf-8 -*-
# @Time     : 2020/11/4 7:03
# @Author   : chw
# @File     : shujujiegou.py


#生成一个平方列表，分别用for循环和列表生成式怎么写
# list_square = []
# for i in range(1,4):
#     list_square.append(i**2)
#
# print(list_square)
# # 列表生成式
# list_square1 = [i**2 for i in range(1,4)]
# print(list_square1)
#
# # 列表生成式带判断
# list_square2 = []
# for i in range(1,4):
#     if i !=1:
#         list_square2.append(i**2)
#
# print(list_square2)
#
# #列表生成式带判断
# list_square3 = [i**2 for i in range(1,4) if i !=1]
# print(list_square3)
#
# # 嵌套循环
# list_square4 = []
# for i in range(1,4):
#     for j in range(1,4):
#         list_square4.append(i*j)
#
# print(list_square4)
#
# # 列表生成式
# list_square5 = [i*j for i in range(1,4) for j in range(1,4)]
# print(list_square5)