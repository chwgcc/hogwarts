# -*- coding: utf-8 -*-
# @Time     : 2020/12/20 10:48
# @Author   : chw
# @File     : test_tag.py
import json

import pytest
import requests

from service.tag import Tag

corpid = 'wwf028ecf95ce7e6f8'
corpsecret = '0UxqJ755htMoGHxHb9NzjM4CXQnXW2f7zErrnRN_JkY'

class TestTag:
    def setup_class(self):
        # todo:数据清理的过程，把测试数据清空或者还原
        self.tag = Tag()
        self.tag.get_token()
    # 获取所有的客户标签
    def test_tag_list(self):
        # todo:完善功能测试
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    # 查询指定的tag_id
    def test_tag_list_appoint(self):
        data = {
            "tag_id": [
                "etM_hZDAAAUAh-rne4sOxOL_t5h9CCzw"
            ]
        }
        r = self.tag.list(tag_id = data)
        # print(f"结果为：{r.json()}")
        print(f"结果为：{json.dumps(r.json(), indent=2)}")


    @pytest.mark.parametrize("group_name, tag_names",[
        ["group_demo_1220",[{'name': "tag_name_1220"}]],
        ["group_demo_1221", [{'name': "tag_name_1221"}, {'name': "tag_name_1222"}]],
    ])
    def test_tag_add(self, group_name, tag_names):

        r = self.tag.add(group_name, tag_names, None)
        assert r.status_code == 200
        # assert r.json()["errcode"] == 0

        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [{'name':tag['name']} for tag in group["tag"]]
        # tags = [{'name': tag['name']} for tag in group['tag']]
        print(group)
        print(tags)

        assert group["group_name"] == group_name
        assert tags == tag_names

    # 向指定的标签组下添加标签,需要填写group_id参数
    @pytest.mark.parametrize("group_name",[
        "demo_1220"
    ])
    def test_tag_add_appoint(self, group_name):
        # 获取group_id
        r = self.tag.list()
        group = [group for group in r.json()["tag_group"] if group['group_name'] == group_name][0]
        group_id = group['group_id']
        # print(group)
        # print(group_id)

        self.tag.add("123", [{"name":"123"}], group_id)
        # 如果填写了group_id参数，则group_name参数会被忽略
        r = self.tag.list()
        group = [group for group in r.json()["tag_group"] if group['group_name'] == group_name][0]
        tags = [{'name':tag['name']} for tag in group["tag"]]

        assert group["group_name"] == group_name
        # 判断新建的tag在tags中
        assert {"name":"123"} in tags

    # 填写的groupname已经存在，则会在此标签组下新建标签
    @pytest.mark.parametrize("group_name", [
        "demo_1220"
    ])
    def test_tag_add_groupnameexit(self, group_name):
        # 标签组内的标签不可同名，如果传入多个同名标签，则只会创建一个
        self.tag.add(group_name, [{"name":'groupnameexit'},{"name":'groupnameexit'}], None)
        r = self.tag.list()
        group = [group for group in r.json()["tag_group"] if group['group_name'] == group_name][0]
        tags = [{'name': tag['name']} for tag in group["tag"]]

        # 获取group_name中tag_name为groupnameexit的个数
        count = str(tags).count("groupnameexit")
        # 断言：有且仅有一个
        assert count == 1

    # 名字超过30字符报错,分三种情况：group.name超出，tag.name超出，两者全超出
    @pytest.mark.parametrize("group_name, tags", [
        ["iamgroupnameistoolangtoolangtoolangtoolang",[{"name": 'chw'}]],
        ["chw",[{"name": 'iamtagnameistoolangtoolangtoolangtoolang'}]],
        ["iamgroupnameistoolangtoolangtoolangtoolang", [{"name": 'iamtagnameistoolangtoolangtoolangtoolang'}]]
    ])

    def test_tag_add_fail(self, group_name, tags):
        r = self.tag.add(group_name, tags, None)
        # 断言，字符超出后的errcode为40058
        assert r.json()["errcode"] == 40058





