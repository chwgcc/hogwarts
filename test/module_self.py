# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 7:45
# @Author   : chw
# @File     : module_self.py

import os
import time

# 创建目录mkdir
# os.mkdir("testdir")
# listdir查看路径下有哪些文件,./代表当前文件
# print(os.listdir("./"))
# removedir删除目录
# os.removedirs("testdir")
# 获取当前路径
# print(os.getcwd())

# 创建b/test.txt路径
# 判断b是否存在
# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt","w")
#     f.write("hello,os using")
#     f.close()


# time模块常用的方法
# 国外的时间格式
# print(time.asctime())
# 时间戳
# print(time.time())
# 等待
# time.sleep()
# 时间戳转成时间元组
# print(time.localtime())
# 将当前的时间戳转成带格式的时间,格式为：time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))

# 获取两天前的时间
# now_timestamp = time.time()
# two_day_before = now_timestamp - 60*60*24*2
# time_tuple = time.localtime(two_day_before)
# print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))


# 标准库urllib
# import urllib.request
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.read())
# 获取响应的头部信息
# print(response.headers)


# math库
import math
# 返回大于等于参数x的最小整数
print(math.ceil(5.5))
# 返回小于等于参数的最大整数
print(math.floor(5.2))
# 平方根
print(math.sqrt(4))


