# -*- coding: utf-8 -*-
# @Time     : 2020/11/10 21:13
# @Author   : chw
# @File     : test_calc.py
import pytest

from test_pytest.core.calc import Calc
class TestCalc:
    # setup_class只在初始化类的时候调用一次
    def setup_class(self):
        self.calc = Calc()
    # setup每次初始化的时候都会调用，而我们只需要调用一次，所以不适合
    # def setup(self):
        # pass

    # 参数化
    @pytest.mark.parametrize('a,b,c',[
        # 正常用例
        [1,2,2],
        [2,4,8],
        # 乘数中有一个为负数
        [1,-1,-1],
        [-2,3,-6],
        # 乘数两个均为负数
        [-2,-8,16],
        # 乘数中有一个为0
        [1,0,0],
        [0,1,0],
        # 两个乘数均为0
        [0,0,0],
        # 乘数中有一个浮点数，结果为整数（不会报错）
        [2.5,2,5],
        [4,1.5,6],
        # 乘数中有一个浮点数，结果也为浮点数（会报错，浮点数相乘bug）
        [6,1.2,7.2],
        [1.1,6,6.6],
        # 乘数中两个均为浮点数(浮点数相乘bug)
        [1.33,2.33,3.0989],
        # 类似于如下的异常单独编写
        # ["a",3,3],
        # [1,2,None]
    ])
    def test_mul(self,a,b,c):
        assert self.calc.mul(a,b) == c

    # 输入的乘数包含非数字的异常情况（这个测试用例要怎么写？？）
    @pytest.mark.parametrize('a,b,c',[
        ['a',3,5],
        [4,'a',7]
    ])
    def test_mul1(self,a,b,c):
        assert self.calc.mul(a,b) == c

    # 输入的参数不够3个的异常（这个怎么写？？？）
    @pytest.mark.parametrize('a,b', [
        [3, 5],
        [4, 7]
    ])
    def test_mul2(self, a, b, c):
        assert self.calc.mul(a, b) == c


    # 以下为除法的参数化
    @pytest.mark.parametrize('i,j,k',[
        # 正常用例
        [8,2,4],
        # 除数与被除数均为负数
        [-10,-5,2],
        # 除数为负数
        [6,-2,-3],
        # 被除数为负数
        [-10,5,-2],
        # 被除数为0
        [0,5,0],
        # 除数为0，单独写
        # [4,0,4],
        # 不能整除的情况
        [1,3,1/3],
        # 结果为浮点数
        [9,4,2.25],
        # 含有浮点数
        [3.2,2,1.6],
        [4.8,1.6,3]
        # 含有非数字的,单独写
        # ['a',10,5],
        # 缺少参数的，单独写
        # [2,3,None]
    ])
    def test_div(self,i,j,k):
        assert self.calc.div(i,j) == k


    # 除数为0的
    @pytest.mark.parametrize('i,j',[
        [2,0],
        [5,0]
    ])
    def test_div1(self,i,j):
        # 括号中为抛出的异常，如果不知道具体的异常就直接使用Exception
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(i,j)

    # 其他异常（包括非数字以及参数不够等，但这样不能为非数字的也会通过，因为只是断言失败）
    @pytest.mark.parametrize('i,j,k', [
        [2, 'q',10],
        [5, 2,None]
    ])
    def test_div2(self, i, j, k):
        # 括号中为抛出的异常，如果不知道具体的异常就直接使用Exception
        with pytest.raises(Exception):
            assert self.calc.div(i, j)


    # 流程实例(先乘后除)
    def test_process(self):
        r1 = self.calc.mul(1,2)
        r2 = self.calc.div(2,1)
        assert r1 == 2
        assert r2 == 2

    # 流程实例(先除后乘)
    def test_process1(self):
        r1 = self.calc.div(10,2)
        r2 = self.calc.mul(2,1)
        assert r1 == 5
        assert r2 == 2
