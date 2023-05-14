# _*_ coding:utf-8 _*_
'''
@File       :conftest.py
@Time       :2023/5/14 21:40
@Author     :且任荣枯
@Version    :1.0

'''
import pytest

@pytest.fixture
def mid(order):
    order.append("mid subpackage")

