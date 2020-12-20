# -*- coding: utf-8 -*-
# @Time     : 2020/12/15 20:17
# @Author   : chw
# @File     : test_auth.py
import requests
from requests.auth import HTTPBasicAuth
def test_auth():
    url = "http://httpbin.testing-studio.com/basic-auth/chw/chw123"
    # 加了认证返回200
    # r = requests.get(url,auth = HTTPBasicAuth("chw","chw123"))
    # 不加认证，返回401
    r = requests.get(url)
    print(r)

