# -*- coding: utf-8 -*-
# @Time     : 2020/11/4 7:17
# @Author   : chw
# @File     : hogwarts_data.py

# 元组的两种定义方式
# tuple_hogwarts = (1,2,3)
# tuple_hogwarts1 = 1,2,3

# 元组的不可变性
# tuple_hogwarts1[0] = "a"
# print(tuple_hogwarts1)

# 如果元组中嵌套了列表，那列表中的元素是可变的
# tuple_test = (1,2,3,[1,2,3])
# tuple_test[3][1] = "a"
# print(tuple_test)

# 集合使用列表生成式
# a = { i for i in "qtwygstijahyysfhjuywtrdwrtqfag"}
# print(a)

# 集合的去重功能,直接使用set
# b = "wytwyvdhgsahsbxjhgsdubchgytwrtyfsfag"
# print(set(b))

# 字典的定义
# 空字典
# dict1 = {}
# # 字典的定义两种方式
# dict2 = {"a":1,"b":2}
# dict3 = dict(a=1,b=2)

# fromkeys的用法
# a= {}
# b = a.fromkeys([1,2,3])
# print(b)
#
# c = a.fromkeys((1,2,3),"a")
# print(c)

# 字典推导式
print({i: i * 2 for i in range(1, 4)})


