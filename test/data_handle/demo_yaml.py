# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 19:45
# @Author   : chw
# @File     : demo_yaml.py

import yaml
# yaml转换为列表
# print(yaml.load("""
#  - A
#  - B
#  - C
#  - D
# """,Loader=yaml.FullLoader))

# yaml转换为字典
# print(yaml.load("""
# A : 1
# """,Loader=yaml.FullLoader))

# 从yaml中读取数据
# print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))

# 将其他格式转换为yaml格式
print(yaml.dump([['H', 'P'], ['A', 'E', 'a:1']]))
print(yaml.dump({"a": [1, 2]}))
# 并放入文件中
with open("demo1.yml","w") as f:
    yaml.dump(data=[['H', 'P'], ['A', 'E', 'a:1']],stream=f)
    yaml.dump(data={"a": [1, 2]},stream=f)
