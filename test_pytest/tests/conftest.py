# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 11:50
# @Author   : chw
# @File     : conftest.py


import pytest

from test_pytest.core.calc import Calc

# pytest中默认将fixture存放在conftest文件中，存在在该文件中的话，使用的时候不需要导入
#
# @pytest.fixture(scope='module')
# def calc_init():
#     print('setup_class已经被fixture优化了')
#
#     return Calc()