# -*- coding: utf-8 -*-
# @Time     : 2020/11/17 20:03
# @Author   : chw
# @File     : test_window_frame.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_webdriver.base import Base

# setup、tesrdown封装在了Base类中，所以想要用得继承这个类
class TestWindowFrame(Base):
    @pytest.mark.skip
    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.LINK_TEXT,'登录').click()
        # print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT,'立即注册').click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        # 切换窗口
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys("username")
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__phone').send_keys("18401588252")
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__password').send_keys("password")
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__verifyCodeSend').click()
        # 切换回原窗口
        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(3)

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 以下两种写法都可以，但推荐使用第一种。
        # self.driver.switch_to.frame("iframeResult")
        self.driver.switch_to_frame("iframeResult")
        # text后面不要加（）
        print(self.driver.find_element(By.ID, 'draggable').text)

        #切换原页面,以下两种均可
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID,'iframewrapper').click()
        sleep(3)






