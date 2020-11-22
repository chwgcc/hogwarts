# -*- coding: utf-8 -*-
# @Time     : 2020/11/19 7:29
# @Author   : chw
# @File     : test_register.py
from pageobject.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        # 通过注册页面去注册
        assert self.main.goto_register().register()

    def test_register1(self):
        # 通过登陆页面的注册去注册
        # 断言根据实际情况以及业务编写
        assert self.main.goto_login().goto_register().register()
