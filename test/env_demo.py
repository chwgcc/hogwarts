# -*- coding: utf-8 -*-
# @Time     : 2020/12/18 7:26
# @Author   : chw
# @File     : env_demo.py
import requests
import yaml

#,encoding="utf-8"
class Api:
    env = yaml.safe_load(open(r"E:\hogwarts_chw\test\env.yaml"))
    # data = {
    #     "method":"get",
    #     "url":"https://www.baidu.com",
    #     "headers":None
    # }
    # data是一个请求的信息
    def send(self, data:dict):
        # 替换                                          self.env["testing"]["dev"]
        data["url"] = str(data["url"]).replace("baidu",self.env["testing"][self.env["default"]])
        r = requests.request(method = data["method"], url = data["url"], headers = data["headers"])
        return r