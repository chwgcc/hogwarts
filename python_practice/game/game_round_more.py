# -*- coding: utf-8 -*-
# @Time     : 2020/10/23 17:12
# @Author   : chw
# @File     : game_round_more.py

# 定义fight函数实现游戏逻辑
def fight():
    # 定义四个变量来存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 199

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        #判断谁的血量小于等于0
        if my_hp <= 0:
            print("我输了")
            #满足条件跳出循环
            break
        if enemy_hp <=0:
            print("我赢了")
            # 满足条件跳出循环
            break

#调用函数fight
fight()
