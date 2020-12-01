# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 15:08
# @Author   : chw
# @File     : loginpage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageobject.podemo.register_page import RegisterPage


class LoginPage:
    # 此处是接收传过来的driver
    # WebDriver为添加类型提示，要不然driver后的find_element等都不会自动提示
    def __init__(self ,driver:WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        # 点击注册按钮
        self.driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        # 进入注册页面
        return RegisterPage(self.driver)