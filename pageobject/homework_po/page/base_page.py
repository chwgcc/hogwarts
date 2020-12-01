# -*- coding: utf-8 -*-
# @Time     : 2020/11/30 6:23
# @Author   : chw
# @File     : base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 不能放在构造函数里面，会报错
    _base_url = ""
    # 构造函数
    def __init__(self, driver:WebDriver = None):
        # 复用浏览器
        if driver == None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            # 如果有传入driver，就使用当前driver
            self.driver = driver
        # 如果传入url，则打开传入url
        if self._base_url != "":
            self.driver.get(self._base_url)
        # 隐式等待
        self.driver.implicitly_wait(5)
    # 封装元素定位
    def find(self, by, calactor):
        return self.driver.find_element(by,calactor)
    # 封装元素定位
    def finds(self, by, calactor):
        return self.driver.find_elements(by,calactor)

    # 显示等待
    def wait_for_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))


