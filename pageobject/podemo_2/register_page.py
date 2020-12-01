# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 15:18
# @Author   : chw
# @File     : register_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self ,driver:WebDriver):
        self.driver = driver

    def register(self):
        # 输入公司名称
        self.driver.find_element(By.ID,'corp_name').send_keys('1234')
        # 输入手机号码
        self.driver.find_element(By.ID,'register_tel').send_keys('18412345678')
        # 点击注册
        self.driver.find_element(By.ID,'submit_btn').click()
        return True
