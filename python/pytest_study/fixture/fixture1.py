# _*_ coding:utf-8 _*_
'''
@File       :fixture1.py
@Time       :2023/5/14 18:50
@Author     :且任荣枯
@Version    :1.0

'''
import pytest


@pytest.fixture
def order():
    return []


@pytest.fixture
def outer(order, inner):
    order.append("outer")


class TestOne:
    @pytest.fixture
    def inner(self, order):
        order.append("one")

    def test_order(self, order, outer):
        assert order == ["one", "outer"]


class TestTwo:
    @pytest.fixture
    def inner(self, order):
        order.append("two")

    def test_order(self, order, outer):
        assert order == ["two", "outer"]