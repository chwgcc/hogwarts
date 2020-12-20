# -*- coding: utf-8 -*-
# @Time     : 2020/12/14 20:08
# @Author   : chw
# @File     : rewrite_xueqiu.py

from mitmproxy import http
import json


def response(flow:http.HTTPFlow):
    # 添加过滤条件，只修改这一个接口数据，否则的话其他接口找不到该字段会报错
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 拿到响应数据，转化成为Python对象
        data = json.loads(flow.response.content)
        # 修改对应的字段的值
        data["data"]["items"][1]["quote"]["name"] *= 2
        data["data"]["items"][2]["quote"]["name"] = ""
        # 把修改后的数据转为字符串，赋值给原始响应数据
        flow.response.text = json.dumps(data)
