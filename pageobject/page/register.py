# -*- coding: utf-8 -*-
# @Time     : 2020/11/19 7:17
# @Author   : chw
# @File     : register.py
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,'corp_name').send_keys("hello")
        self.find(By.ID,'manager_name').send_keys("hello")
        return True
