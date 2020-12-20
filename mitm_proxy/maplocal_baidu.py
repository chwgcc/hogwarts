# -*- coding: utf-8 -*-
# @Time     : 2020/12/14 7:08
# @Author   : chw
# @File     : maplocal_baidu.py

from mitmproxy import http

# 方法名request不可以修改
def request(flow: http.HTTPFlow):
    # 发起请求，判断url是不是预期的值
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 创造一个response
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )