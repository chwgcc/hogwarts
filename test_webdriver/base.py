# -*- coding: utf-8 -*-
# @Time     : 2020/11/17 20:05
# @Author   : chw
# @File     : base.py
import os

from selenium import webdriver


class Base():
    def setup(self):
        # 实现多浏览器访问
        browser = os.getenv("browser")
        if browser == 'edge':
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()