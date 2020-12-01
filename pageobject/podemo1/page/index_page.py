# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 15:57
# @Author   : chw
# @File     : index_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pageobject.podemo1.page.addmember_page import AddMemberPage
from pageobject.podemo1.page.base_page import BasePage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     self.driver.implicitly_wait(5)

    def click_add_member(self):
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)