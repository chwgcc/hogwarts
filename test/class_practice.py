# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 7:16
# @Author   : chw
# @File     : class_practice.py

# 通过class 关键字定义类
class Person:
    # 类变量
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    # 构造函数，在实例化的时候会被执行
    def __init__(self,name,age,gender,weight):
        # 通过self.访问到的变量，为实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
    # def set_name(self,name):
    #     self.name = name
    #
    # def set_age(self,age):
    #     self.age = age

    # 想要访问类方法，需要加一个装饰器@classmethod,这个只针对一个方法有效，想要多个方法都能被访问，需要在每个方法前加上@classmethod
    @classmethod
    def eat(self):
        print(f"{self.name} is eating")

    def play(self):
        print(f"{self.name} is playing")

    def jump(self):
        print(f"{self.name} is jump")

# 实例化
zs = Person("zhangsan",20,"male",80)
# zs.set_name("zhangsan")
# zs.set_age(30)
print(f"zs的姓名为：{zs.name},zs的年龄为：{zs.age},zs的性别为{zs.gender},zs的体重为{zs.weight}")
zs.eat()
zs.play()
zs.jump()

# 类变量和实例变量的区别：类变量通过类来访问，实例变量通过实例来访问
# 打印类变量与实例变量
# print(Person.name)
# print(zs.name)
# # 修改类变量与实例变量
# Person.name = "chw"
# zs.name = "gcc"
# print(Person.name)
# print(zs.name)

# 类方法和实例方法:类方法是不能访问实例方法的
Person.eat()


