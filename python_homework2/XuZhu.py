# -*- coding: utf-8 -*-
# @Time     : 2020/10/31 8:43
# @Author   : chw
# @File     : XuZhu.py


# 定义XuZhu类,继承童姥类
from python_homework2.TongLao import TongLao


class XuZhu(TongLao):
    # 定义read方法
    def read(self):
        print("罪过罪过")
    # 定义劝架方法
    def quanjia(self):
        # 调用父类的打架函数
        super().fight_zms(200,500)
        # 调用同一class中不同的方法可以用类名.方法实现
        XuZhu.read(self)



# 实例化
xuzhu = XuZhu(400,200)
xuzhu.quanjia()
