# -*- coding: utf-8 -*-
# @Time     : 2020/12/6 14:38
# @Author   : chw
# @File     : test_demo.py
import requests
from jsonpath import jsonpath
from hamcrest import *


class TestDemo:
    def test_get(self):
        r = requests.get("http://httpbin.testing-studio.com/get")
        print(r.json())
        print(r.text)
        print(r.status_code)
        assert r.status_code == 200
    # get请求,query
    def test_query(self):
        param = {
            "name":"chw",
            "age":18
        }
        headers = {
            "Cont123":"1234",
            "Connection": "close1",
            "User-Agent":"python"
        }
        r = requests.get("http://httpbin.testing-studio.com/get",params=param,headers=headers)
        print(r.json())
        print(r.text)
        assert r.status_code == 200
        # 获取json中对应的数值，使用这种方法
        assert r.json()["headers"]["Cont123"] == "1234"
        assert r.json()["args"]["name"] == "chw"

    def test_post_form(self):
        datas = {
            "name":"chw",
            "age":18
        }

        r = requests.post("http://httpbin.testing-studio.com/post",data=datas)
        print(r.text)
        assert r.status_code == 200


    def test_post_json(self):
        datas = {
            "name":"chw",
            "age":18
        }

        r = requests.post("http://httpbin.testing-studio.com/post",json=datas)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["name"] == "chw"


    def test_hogwarts_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        # print(r.text)
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"
        # 使用jsonpath断言，与xpath类似
        assert jsonpath(r.json(),'$..name')[0] == "开源项目"
        # 取出json中所有key为name的value值
        print(jsonpath(r.json(), '$..name'))

    # 复杂的断言可以使用hamcrest
    def test_hamcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        # print(r.text)
        assert r.status_code == 200
        # assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"
        # 此断言与上一句一样的意思
        assert_that(r.json()["category_list"]["categories"][0]["name"],equal_to("开源项目"))
