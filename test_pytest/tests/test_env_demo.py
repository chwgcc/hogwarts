# -*- coding: utf-8 -*-
# @Time     : 2020/12/18 7:33
# @Author   : chw
# @File     : test_env_demo.py

from test import env_demo
def test_send():
    data = {
        "method": "get",
        "url": "https://www.baidu.com",
        "headers": None
    }
    api = env_demo.Api()
    res = api.send(data)
    print(res.text)
