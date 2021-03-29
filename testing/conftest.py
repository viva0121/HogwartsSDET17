# conftest.py 文件名是固定的，不能改
# import datetime
import pytest

from pythoncode.Calculator import Calculator
from testing.test_calculator_fixture import get_datas


@pytest.fixture()
def get_instance():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_data_with_fixture(request):
    return request.param

# @pytest.fixture(scope='session')
# def login():
#     print("登录操作>>>>>>")
#     token = datetime.datetime.now()
#     yield token
#     print("登出操作")
