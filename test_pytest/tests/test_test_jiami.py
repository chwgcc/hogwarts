# -*- coding: utf-8 -*-
# @Time     : 2020/12/15 21:04
# @Author   : chw
# @File     : test_test_jiami.py

from test import test_jiami
class TestApiRequest:
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_send(self):
        ar = test_jiami.ApiRequest()
        print(ar.send(self.req_data))
