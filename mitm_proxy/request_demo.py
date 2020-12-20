# -*- coding: utf-8 -*-
# @Time     : 2020/12/13 20:25
# @Author   : chw
# @File     : request_demo.py

from mitmproxy import http
def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"] = "chw"
    print(flow.request.headers)