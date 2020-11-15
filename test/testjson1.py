# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 6:36
# @Author   : chw
# @File     : testjson1.py

# json 由字典和列表组成的
import json

data = {
    "name":["jerry","nickname"],
    "age": 26,
    "gender":"female"
}

print(type(data))
data1 = json.dumps(data)
print(data1)
print(type(data1))

data2 = json.loads(data1)
print(type(data2))