from decimal import Decimal

import pytest
import yaml

import sys

sys.path.append("..")
from pythoncode.Calculator import Calculator


# 获取yaml文件中的测试数据和对应的ids
def get_datas(name, type):
    with open("./datas/calc.yml") as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas, ids)


class TestCalc:
    # 传入各种类型的测试数据，并赋值
    add_int_data = get_datas('add', 'int')
    add_float_data = get_datas('add', 'float')
    add_string_data = get_datas('add', 'string')
    div_int_normal = get_datas('div', 'int_normal')
    div_int_error = get_datas('div', 'int_error')
    div_float_data = get_datas('div', 'float')

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # 加法
    # 整数相加
    @pytest.mark.parametrize("a,b,result", add_int_data[0], ids=add_int_data[1])
    def test_add_int(self, a, b, result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.add(a, b)

    # 小数相加
    @pytest.mark.parametrize("a,b,result", add_float_data[0], ids=add_float_data[1])
    def test_add_float(self, a, b, result):
        print(f"a={a},b={b},result={result}")
        # assert result == round(self.calc.add(a, b),2)
        assert round(Decimal(result), 2) == round(self.calc.add(Decimal(a), Decimal(b)), 2)

    # 字符串相加
    @pytest.mark.parametrize("a,b,result", add_string_data[0], ids=add_string_data[1])
    def test_add_string(self, a, b, result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.add(a, b)

    # 相除功能
    # 除数不为0的整数(+/-)，被除数(+,0,-)
    @pytest.mark.parametrize("a,b,result", div_int_normal[0], ids=div_int_normal[1])
    def test_div_int(self, a, b, result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.div(a, b)

    # 除数为0
    # 除数为0
    @pytest.mark.parametrize("a,b,result", div_int_error[0], ids=div_int_error[1])
    def test_div_error(self, a, b, result):
        with pytest.raises(Exception):
            a / b

    @pytest.mark.parametrize("a,b,result", div_float_data[0], ids=div_float_data[1])
    def test_div_float(self, a, b, result):
        print(f"a={a},b={b},result={result}")
        assert result == round(self.calc.div(a, b), 2)
