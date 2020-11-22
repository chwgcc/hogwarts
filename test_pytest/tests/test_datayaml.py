# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 13:03
# @Author   : chw
# @File     : test_datayaml.py
import pytest
import yaml

from test_pytest.core.calc import Calc

def load_data(path='data.yaml'):
    with open(path,'rb') as f:
        data = yaml.safe_load(f)
        keys=",".join(data[0].keys())
        values=[d.values() for d in data]
        return {'keys':keys,'values':values}


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    @pytest.mark.parametrize(load_data()['keys'],load_data()['values'])
    def test_div(self,a,b,c):
        assert self.calc.div(a,b) == c

