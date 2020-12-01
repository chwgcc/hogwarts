# -*- coding: utf-8 -*-
# @Time     : 2020/11/30 6:24
# @Author   : chw
# @File     : index_page.py
from selenium.webdriver.common.by import By

from pageobject.homework_po.page.addmember_page import AddMemberPage
from pageobject.homework_po.page.base_page import BasePage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def click_addmember(self):
        self.find(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
        return AddMemberPage(self.driver)

