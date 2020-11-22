# -*- coding: utf-8 -*-
# @Time     : 2020/11/18 20:52
# @Author   : chw
# @File     : main.py
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage
from pageobject.page.login import Login
from pageobject.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    def goto_register(self):
        self.find(By.XPATH,"//*[@class='index_head_info_pCDownloadBtn']").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.XPATH,"//*[@class='index_top_operation_loginBtn']").click()
        return Login(self._driver)