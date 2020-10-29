# -*- coding: utf-8 -*-
# @Time     : 2020/10/30 7:30
# @Author   : chw
# @File     : houyi.py

# 定义HouYi类
from python_practice.python_class.game_oop import Game


class HouYi(Game):
    # 定义构造函数
    def __init__(self,my_hp, enemy_hp):
        self.defense = 100
        # 通过super调用父类的构造方法，就可以直接拿到父类的属性
        super().__init__(my_hp, enemy_hp)
    # 改造fight函数
    def fight(self):
        while True:
            # 加上护甲值
            self.my_hp = self.my_hp + self.defense - self.enemy_power
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



houyi = HouYi(1000,1100)
houyi.fight()
# 子类对象可以直接调用父类方法
houyi.rest(5)
