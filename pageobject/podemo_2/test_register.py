# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 15:29
# @Author   : chw
# @File     : test_register.py
from pageobject.podemo.main_page import MainPage


class TestRegister:
    def setup(self):
        self.main = MainPage()

    def test_register(self):
        # 通过点击注册按钮
        # result = self.main.goto_register().register()
        # 通过点击登录页面的注册按钮
        result= self.main.goto_login().goto_register().register()
        # 断言
        assert result
