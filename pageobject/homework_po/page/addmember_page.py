# -*- coding: utf-8 -*-
# @Time     : 2020/11/30 6:24
# @Author   : chw
# @File     : addmember_page.py
from selenium.webdriver.common.by import By

from pageobject.homework_po.page.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self, name, account, phone):
        # name = "aaaa"
        # account = "1234567"
        # phone = "18401566787"
        self.find(By.ID, 'username').send_keys(name)
        # 输入账号
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        # 选择性别
        self.find(By.XPATH, '//input[@value=2]').click()
        # 输入手机号
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()
        # self.driver.find_element(By.XPATH, '//*[@class="js_member_editor_form"]/div[3]/a[2]').click()
        return True

    def get_member(self, value):
        # 加入隐式等待
        locator = (By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_for_click(locator)

        title_total = []
        while True:
            elements = self.finds(By.XPATH,'//*[@class="member_colRight_memberTable_tr  member_colRight_memberTable_tr_Inactive"]/td[2]')
            titles = [element.get_attribute("title") for element in elements]
            if value in titles:
                return True
            title_total.extend(titles)

            page: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total = page.split('/',1)

            if num == total:
                return False
            else:
                self.find(By.CSS_SELECTOR, ".js_next_page").click()







