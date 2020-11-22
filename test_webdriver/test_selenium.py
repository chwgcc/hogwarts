# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 14:58
# @Author   : chw
# @File     : test_selenium.py

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        # 浏览器的最大化
        self.driver.maximize_window()
        # 打开百度首页
        self.driver.get("https://www.baidu.com/")
        # 添加隐式等待5秒
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        # 资源回收，关闭浏览器
        # self.driver.quit()

    def test_hogwarts(self):
        # 使用xpath定位
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # 使用ID定位
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试学院")
        # 使用css_selector定位
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("霍格沃兹测试学院")
        # 点击百度一下按钮
        self.driver.find_element(By.ID,'su').click()
