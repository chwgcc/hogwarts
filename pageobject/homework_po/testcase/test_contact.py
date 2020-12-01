# -*- coding: utf-8 -*-
# @Time     : 2020/11/30 6:25
# @Author   : chw
# @File     : test_contact.py
from pageobject.homework_po.page.index_page import IndexPage


# class TestContact:
#     def setup(self):
#         self.index = IndexPage()

class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        name = "aaaa"
        account = "1234567"
        phone = "18401566787"
        # 先将页面存下来，后续可以直接调用多个方法
        addmemberpage= self.index.click_addmember()
        addmemberpage.add_member(name, account, phone)
        result = addmemberpage.get_member(name)
        assert result



