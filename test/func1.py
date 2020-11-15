# -*- coding: utf-8 -*-
# @Time     : 2020/11/1 8:12
# @Author   : chw
# @File     : func1.py

def func1(a):
    """
    #在函数中输入两个双引号，再enter一下，会出现函数说明，类似于注释，给开发者看的，在此可以添加注释
    :param a:参数a是用来打印的
    :return:
    """
    print(f"这是一个参数{a}")


# 默认参数在定义函数的时候使用k=v的形式定义
# 调用函数的时候，如果没有传递参数，则会使用默认参数
# 如果传递参数的话，则会使用传递的参数
def func2(a=1):
    print(f"参数a的值为{a}")

# 这样调用会返回默认值1
# func2()

# 这样调用会返回传入值
# func2(2)

"""
关键字参数
在调用函数的时候，使用k=v的方式进行传参
在函数调用/定义中，关键字参数必须跟随在位置参数的后面
"""
def func3(a,b,c):
    print(f"参数a的值为{a}")
    print(f"参数b的值为{b}")
    print(f"参数c的值为{c}")

# 全部指定时可以不考虑位置
# func3(b=3,c=1,a=5)
# 指定部分的时候，关键字参数必须跟在位置参数的后面，如下会报错
# func3(b=2,a=5,7)
# 指定部分的时候，每个参数只能接收一个值，否则会报错
# func3(2,a=3,b=4)

#func3(7,c=3,b=5)





# lambda表达式
func4 = lambda x : x*2
# print(func4(5))

#以上面的lambda函数一样
def func5(x):
    return x*2
# print(func5(6))

# 含有多个参数的lambda表达式
func6 = lambda x,y : x + y
print(func6(1, 2))