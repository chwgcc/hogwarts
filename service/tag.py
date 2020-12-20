# -*- coding: utf-8 -*-
# @Time     : 2020/12/20 11:52
# @Author   : chw
# @File     : tag.py


# 因为这两个是企业微信公用的，不是类里面的，所以就先放在这
import json

import requests

corpid = 'wwf028ecf95ce7e6f8'
corpsecret = '0UxqJ755htMoGHxHb9NzjM4CXQnXW2f7zErrnRN_JkY'
class Tag:

    def __init__(self):
        self.token = ""

    def get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={'corpid': corpid, 'corpsecret': corpsecret}
                         )
        print(json.dumps(r.json(), indent=2))
        # 因为token后续都需要使用，所以将token放到实例中（初始化）去
        self.token = r.json()["access_token"]

    def list(self, **tag_id):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                           params={"access_token": self.token},
                           json={
                               "tag_id": tag_id
                           }
                           )
        # 将响应信息pretty，看起来更方便,indent=2间隔为两个空格
        print(json.dumps(r.json(), indent=2))
        # 返回响应结果，也可以return r.json()
        return r

    def add(self, group_name, tags, group_id):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "group_name": group_name,
                              "tag": tags,
                              "group_id": group_id
                          }
                          )
        print(json.dumps(r.json(), indent=2))
        return r