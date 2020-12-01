# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 14:58
# @Author   : chw
# @File     : main_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.podemo.loginpage import LoginPage
from pageobject.podemo.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def goto_login(self):
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        # 进入登录页面
        return LoginPage(self.driver)

    def goto_register(self):
        # 点击注册按钮
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        # 进入注册页面
        return RegisterPage(self.driver)