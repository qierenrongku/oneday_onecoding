# _*_ coding:utf-8 _*_
'''
@File       :conftest.py
@Time       :2023/5/14 21:39
@Author     :且任荣枯
@Version    :1.0

'''
import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def top(order, innermost):
    order.append('top')

