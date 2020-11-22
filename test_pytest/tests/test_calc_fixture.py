# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 10:07
# @Author   : chw
# @File     : test_calc_fixture.py
import allure
import pytest
import yaml

from test_pytest.core.calc import Calc


# 读取yaml文件中的数据

def load_data(path='data.yaml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        keys=",".join(data[0].keys())
        values=[d.values() for d in data]
        return {'keys':keys,'values':values}

class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    # setup_class后的参数也可以使用cls,两种写法其实是一样的，但cls需要添加@classmethod
    # 当两者同时存在时，该方法会覆盖上面的方法
    # @classmethod
    # def setup_class(cls):
    #     print("setup_class classmethod")
    #     cls.calc=Calc()



    # # 报告中添加步骤
    # @allure.step
    # def simple_step(self,step_param1, step_param2=None):
    #     pass

    # # 参数化
    # @pytest.mark.parametrize('a,b,c',[
    #     # 正常用例
    #     [1,2,2],
    #     [2,4,8],
    #     # 乘数中有一个为负数
    #     [1,-1,-1],
    #     [-2,3,-6],
    #     # 乘数两个均为负数
    #     [-2,-8,16],
    #     # 乘数中有一个为0
    #     [1,0,0],
    #     [0,1,0],
    #     # 两个乘数均为0
    #     [0,0,0],
    #     # 乘数中有一个浮点数，结果为整数（不会报错）
    #     [2.5,2,5],
    #     [4,1.5,6],
    #     # 乘数中有一个浮点数，结果也为浮点数（会报错，浮点数相乘bug）
    #     [6,1.2,7.2],
    #     [1.1,6,6.6],
    #     # 乘数中两个均为浮点数(浮点数相乘bug)
    #     [1.33,2.33,3.0989],
    #     # 类似于如下的异常单独编写
    #     # ["a",3,3],
    #     # [1,2,None]
    # ])
    # def test_mul(self,a,b,c):
    #     # 添加图片
    #     allure.attach.file(
    #         # 不允许使用远程图片，只能使用本地图片
    #         # 'https://www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png',
    #         # 本地图片(直接复制的话，关注一下/还是\)
    #         'C:/Users/changhongwei/Pictures/Camera Roll/300300.jpg',
    #         # 图片名称
    #         "百度一下",
    #         # 图片类型（加不加attachment_type=都可以）
    #         attachment_type=allure.attachment_type.JPG
    #     )
    #     # 添加步骤
    #     self.simple_step(f"{a} {b} {c}")
    #     assert self.calc.mul(a,b) == c

    # 以下为除法的参数化
    # 通过yaml中的数据传入参数
    @pytest.mark.parametrize(load_data()['keys'],load_data()['values'])
    def test_div(self,i,j,k):
        assert self.calc.div(i,j) == k






