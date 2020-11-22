# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 11:47
# @Author   : chw
# @File     : test_addmember.py
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWX2:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_addmember(self):
        db = shelve.open('cookies')
        # 找到数据之后存放在cookies中
        cookies = db['cookie']
        db.close()

        # 打开企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 加入cookie信息
        for cookie in cookies:
            # 因为expiry必须为整形，且在服务器端存储了一份，这个可以去掉
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()
        # 找到添加联系人并点击
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # 输入姓名
        self.driver.find_element(By.ID,'username').send_keys('aaa')
        # 输入账号
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('123457')
        # 选择性别
        self.driver.find_element(By.XPATH,'//input[@value=2]').click()
        # 输入手机号
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('18401588887')
        # 点击保存按钮
        self.driver.find_element(By.XPATH,'//*[@class="js_member_editor_form"]/div[3]/a[2]').click()
        # 获取联系人姓名
        name = self.driver.find_element(By.XPATH,'//*[@data-type="member"][1]//td[2]').text
        # 断言
        assert "aaa" == name
        sleep(3)
