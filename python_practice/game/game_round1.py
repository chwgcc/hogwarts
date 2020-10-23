# -*- coding: utf-8 -*-
# @Time     : 2020/10/23 16:54
# @Author   : chw
# @File     : game_round1.py

# 定义fight函数实现游戏逻辑
def fight():
    # 定义四个变量来存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 定义最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    #判断输赢
    #注释的快捷键Ctrl+/
    #复制当前行的代码：Ctrl+d
    # if my_final_hp  > enemy_final_hp:
    #     print("我赢了")
    # elif my_final_hp < enemy_final_hp:
    #     print("我输了")
    # else:
    #     print("平局")

    #使用三目运算(只有简单的if else可以这么写，稍微带有elif的就不能使用这种写法)
    print("我赢了") if my_final_hp  > enemy_final_hp else print("我输了")

#调用fight函数
fight()


