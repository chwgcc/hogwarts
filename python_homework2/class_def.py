# -*- coding: utf-8 -*-
# @Time     : 2020/10/31 6:42
# @Author   : chw
# @File     : class_def.py


# 定义动物类
class Animal:
    # 定义名字
    name = "pipi"
    # 定义类型
    type = "dog"

    # 定义方法eat
    def eat(self):
        print("特别能吃")

    # 定义方法bark
    def bark(self,type):
        if type == "dog":
            print("wangwang")
        elif type == "cat":
            print("miaomiao")
        else:
            print("你猜")

# 实例化
pipi = Animal()
# 注意：调用属性的时候需要print一下
print(pipi.type)
# 注意：调用方法的时候不需要再次print，否则输出结果会多出一行none
pipi.eat()
pipi.bark(pipi.type)






# 定义学生类
class Student:
    # 学号
    sid = "20102185"
    # 姓名
    name = "zhangsan"
    # 分数
    score = "576"

    # 方法：参加考试
    def exam(self,name,score):
        print(f"{name}参加考试，得了{score}分")

    # 方法：上课
    def attendclass(self):
        print("学生就应该好好上课")

    # 方法：打游戏
    def playgame(self,time):
        self.time = time
        if self.time > 1:
            print("不要长时间玩游戏，伤身体")
        else:
            print("小玩怡情，你做的很棒")

# 实例化
chw = Student()
print(chw.exam("chw",598))
print(chw.playgame(10))






# 定义person_info类
class person_info:
    # 定义属性，参数形式传入
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    # 定义方法work
    def work(self):
        if self.age > 60:
            print("可以退休了，安享晚年吧")
        else:
            print("每天都得上班，好想退休啊")

# 实例化
gcc = person_info("gcc",61,172)
print(f"{gcc.name}的年龄为{gcc.age}岁")
gcc.work()





# 定义类
class Works:
    #定义属性，传参
    def __init__(self,name,type,salary,time1):
        self.name = name
        self.type = type
        self.salary = salary
        self.time1 = time1

    # 定义方法
    def working(self):
        if self.time1 <= 8:
            print("不加班，好幸福啊")
            if self.salary >= 10000:
                print("挣钱真香")
        else:
            print("好想钱多事少离家近")

#实例化
ceshi = Works("测试","打工狗",11000,9)
print(ceshi.name)
ceshi.working()





# 定义car类
class car:
    # 定义属性
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    #定义方法:返回车的整体信息
    def car_info(self):
        print(f"{self.make}{self.model}生产于{self.year}年")

#实例化
baoma = car("baoma","A6",1998)
baoma.car_info()










