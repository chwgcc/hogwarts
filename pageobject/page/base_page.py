# -*- coding: utf-8 -*-
# @Time     : 2020/11/18 20:54
# @Author   : chw
# @File     : base_page.py
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self,driver:WebDriver=None):
        # 声明一个空值，被调用时可以直接传入该参数（若直接在判断语句中会报错）
        self._driver = ""
        # 判断是否传入driver，传入的话直接使用，没有传入的话实例化，避免页面很多时需要初始化很多次
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)