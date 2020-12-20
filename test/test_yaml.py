# -*- coding: utf-8 -*-
# @Time     : 2020/12/20 9:40
# @Author   : chw
# @File     : test_yaml.py

import yaml
# 转换为yaml，以免自己写yaml文件出错
def test_yaml():
    env = {
        "default": "test",
        "testing":
            {"dev": "baidu",
             "test": "jd"
             }
    }
    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env,stream=f)