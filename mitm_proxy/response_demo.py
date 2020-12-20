# -*- coding: utf-8 -*-
# @Time     : 2020/12/14 19:57
# @Author   : chw
# @File     : response_demo.py
from pprint import pprint

from mitmproxy import http


def response(flow:http.HTTPFlow):
    pprint(flow.response.content)
