# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 7:06
# @Author   : chw
# @File     : test_alluremode.py

import pytest
def test_success():
    assert True

def test_failure():
    assert False

def test_skip():
    pytest.skip("for a reason!")

def test_broken():
    raise Exception("oops")