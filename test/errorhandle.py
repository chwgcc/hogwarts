# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 6:47
# @Author   : chw
# @File     : errorhandle.py

# try:
#     num1 = int(input("请输入一个除数："))
#     num2 = int(input("请输入一个被除数："))
#     print(num1/num2)
# # except ZeroDivisionError:
# #     print("被除数不能为0")
# # except ValueError:
# #     print("需要输入数值型整数")
# # 当不知道异常名字的时候可以直接使用except
# except:
#     print("这是一个通用型异常")
# # 程序没有发生异常时执行else语句
# else:
#     print("程序没有发生异常")
#
# # 不管程序是否发生异常，均执行finally语句
# finally:
#     print("无论发没发生异常均执行")

# 抛出异常
# x = 10
# if x > 5:
#     raise Exception("这是抛出的异常信息")

# 自定义抛出异常
class MyException(Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

raise MyException("value1","value2")