# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 16:05
# @Author   : chw
# @File     : addmember_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):

    # def __init__(self ,driver):
    #     self.driver = driver

    def add_member(self ,name ,account ,phone):
        # 参数可以放到测试用例里面
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
        # 点击保存按钮,如果页面上相同属性的元素有多个，那么通过find_element定位到的元素为第一次出现的元素
        # (之前一直找不到元素，是因为复制出来的class名把.搞成了空格)，以后要多加注意此处
        self.find(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()
        # self.driver.find_element(By.XPATH, '//*[@class="js_member_editor_form"]/div[3]/a[2]').click()
        return True

    def get_member(self, value):
        # 加入显示等待，针对于某个元素的，该页面可能加载比较慢，不是全局的
        locator = (By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_for_click(locator)
        # 已经被封装了
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # find_elements返回的是元素列表[element1,element2,...]
        # 只是查找第一页的情况
        # elements = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        # # 使用列表表达式
        # titles = [element.get_attribute("title") for element in elements]
        # for element in elements:
        #     titles.append(element.get_attribute("title"))
        # 以下为查找全部页的情况
        title_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titles = [element.get_attribute("title") for element in elements]
            if value in titles:
                return True
            title_total.extend(titles)

            page: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = page.split("/", 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".js_next_page").click()

        # return title_total






























        return titles