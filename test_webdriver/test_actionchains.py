# -*- coding: utf-8 -*-
# @Time     : 2020/11/16 6:49
# @Author   : chw
# @File     : test_actionchains.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    # 该条用例跳过，不执行
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("https://www.baidu.com/")
        ele_click = self.driver.find_element(By.ID,'lg')
        # ele_right = self.driver.find_element(By.CSS_SELECTOR,'#u a:nth-child(1)')
        # ele_double = self.driver.find_element(By.XPATH,'//*[@id="con-ar"]/div/div/div/div[1]/a/i')
        action = ActionChains(self.driver)
        action.click(ele_click)
        sleep(3)
        # action.context_click(ele_right)
        # sleep(3)
        # action.double_click(ele_double)
        # sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID,'s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        sleep(3)
        action.perform()

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element(By.ID,'dragger')
        ele_drop = self.driver.find_element(By.XPATH,"//*[text()='Item 1']")
        action = ActionChains(self.driver)
        # 此为一种方式
        # action.drag_and_drop(ele_drag,ele_drop).perform()
        # 第二种方式
        # action.click_and_hold(ele_drag).release(ele_drop).perform()
        # 第三种方式
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)