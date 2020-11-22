# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 11:31
# @Author   : chw
# @File     : test_fixture_demo.py


# 如果fixture存放在其他py文件中，使用的时候需要使用下面的方法导入，否则会报错
# from test_pytest.tests.fixture1 import calc_init
# 如果fixture放在conftest.py文件中，使用的时候可以不导入直接使用


# fixture的使用,注意calc_init后面不要加（）
def test__calc_demo(calc_init):
    assert calc_init.mul(1, 2) == 2


def test__calc_demo2(calc_init):
    assert calc_init.mul(1, 3) == 3


# 用例中也可以不使用fixture
def test__calc_demo3():
    assert 3 == 3