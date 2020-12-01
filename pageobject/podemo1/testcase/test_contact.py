# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 16:17
# @Author   : chw
# @File     : test_contact.py
from pageobject.podemo1.page.index_page import IndexPage


class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        name = "aaaa"
        account = "1234567"
        phone = "18401566787"
        # 只调用一个方法时可以这么用
        # result = self.index.click_add_member().add_member(name, account, phone)
        # 先将页面存下来，后续可以直接调用多个方法
        addmemberpage = self.index.click_add_member()
        addmemberpage.add_member(name, account, phone)
        result = addmemberpage.get_member(name)
        # assert name in result
        assert result

