# -*- coding: utf-8 -*-
# @Time     : 2020/10/28 18:00
# @Author   : chw
# @File     : python_oop.py

#类中的类属性与类方法没有固定的位置，可先可后
#类名的命名规则要遵循驼峰法，首字母要大写

class House:
    #静态属性->类变量（类之中，方法之外）
    door = 'red'
    floor = 'white'

    # 构造函数，在类实例化的时候会直接执行
    def __init__(self):
        #在方法当中调用类变量需要加上self.
        print(self.door)
        # 实例变量一般放在构造函数中,类当中，方法当中，以“self.变量名”方式去定义
        self.kitchen = "cook"

    # 动态方法
    def sleep(self):
        # 普通变量：类当中，方法当中，前面没有self，在当前方法中可以直接调用
        bed = "席梦思"
        self.table = "桌子可以放东西"
        print(f"在房子里可以躺在{bed}上睡觉")

    def cook(self):
        print("在房子里可以做饭")
        print(self.kitchen)
        print(self.table)


# 把类实例化
# 北欧风房子
north_house = House()
# 中式风房子
china_house = House()
# 普通变量在当前方法可以直接调用
north_house.sleep()
north_house.cook()

# 调用类属性
# print(House.door)
# # 修改类属性
# House.door = "white"
# print(House.door)
# # 实例对象调用类属性
# print(north_house.door)
# 修改对象属性
north_house.door = 'black'
print(north_house.door)
print(House.door)
print(china_house.door)


