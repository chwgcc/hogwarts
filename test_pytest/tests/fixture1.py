# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 11:45
# @Author   : chw
# @File     : fixture1.py
import pytest

from test_pytest.core.calc import Calc


 # 查看函数源码的快捷键：ctrl+点击函数名称

# 想要fixture在某一个类中只执行一次，需要修改fixture的scope参数，该参数的默认值为function，即在每一个方法中都执行一次
# scope的可选参数为：function、class、module、package、session（只执行一次）
@pytest.fixture(scope='module')
# fixture可以给你的setup起你想要的的名字，以及可以在其他类中使用
def calc_init():
    print('setup_class已经被fixture优化了')

    return Calc()