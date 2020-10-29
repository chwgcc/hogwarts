# -*- coding: utf-8 -*-
# @Time     : 2020/10/28 20:24
# @Author   : chw
# @File     : game_oop.py

class Game:
    def __init__(self, my_hp, enemy_hp):
        # 定义四个变量来存放数据
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199

    def fight(self):
        # 加入循环，让游戏可以进行多轮
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)

            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                print("我输了")
                # 满足条件跳出循环
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                # 满足条件跳出循环
                break
    def rest(self,time_num):
        print(f"太累了，休息{time_num}分钟")
