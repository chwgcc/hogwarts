# -*- coding: utf-8 -*-
# @Time     : 2020/10/31 7:52
# @Author   : chw
# @File     : TongLao.py


"""
    定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
    1.see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”
    2.fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
    •定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    •加入模块化改造
"""
# 定义一个天山童姥类
class TongLao:
    # 定义属性：属性有血量，武力值（通过传入的参数得到
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    #定义see_people方法
    def see_people(self,name):
        if name == "WYZ":
            print("师弟！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("你这个人我看不见，哈哈")

    # 定义fight_zms方法
    def fight_zms(self,enemy_hp,enemy_power):
        self.hp = self.hp / 2
        # print(self.hp)
        self.power = self.power * 10
        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        # 打印一下各自的血量
        print(f"我的血量为：{self.hp}，敌人的血量为{enemy_hp}")
        # 练习一下三目表达式
        print("我赢了") if self.hp > enemy_hp else print("我输了")



# 实例化
# 注意一下参数的顺序，在这里就因为两者不一致导致了混乱
tl = TongLao(400,200)
# print(tl.hp)
# tl.see_people("丁春秋")
tl.fight_zms(2000,200)




