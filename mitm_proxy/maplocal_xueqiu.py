# -*- coding: utf-8 -*-
# @Time     : 2020/12/14 7:23
# @Author   : chw
# @File     : maplocal_xueqiu.py


from mitmproxy import http

# 方法名request不可以修改
def request(flow: http.HTTPFlow):
    # 发起请求，判断url是不是预期的值
    if "quote.json" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open (r"E:\hogwarts_chw\mitm_proxy\quote1.json",encoding="utf-8") as f:
            # 创造一个response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件中的数据作为返回内容
                f.read(),
                {"Content-Type": "application/json"}  # (optional) headers
            )