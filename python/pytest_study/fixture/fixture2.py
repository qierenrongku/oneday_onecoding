# _*_ coding:utf-8 _*_
'''
@File       :fixture2.py
@Time       :2023/5/14 22:02
@Author     :且任荣枯
@Version    :1.0

'''
import pytest


@pytest.fixture(scope="session")
def order():
    return []


@pytest.fixture
def func(order):
    order.append("function")


@pytest.fixture(scope="class")
def cls(order):
    order.append("class")


@pytest.fixture(scope="module")
def mod(order):
    order.append("module")


@pytest.fixture(scope="package")
def pack(order):
    order.append("package")


@pytest.fixture(scope="session")
def sess(order):
    order.append("session")


class TestClass:
    def test_order(self, func, cls, mod, pack, sess, order):
        assert order == ["session", "package", "module", "class", "function"]