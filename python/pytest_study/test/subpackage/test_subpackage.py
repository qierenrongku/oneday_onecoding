# _*_ coding:utf-8 _*_
'''
@File       :test_subpackage.py
@Time       :2023/5/14 21:40
@Author     :且任荣枯
@Version    :1.0

'''
import pytest

@pytest.fixture
def innermost(order, mid):
    order.append('innermost subpackage')

def test_order(order, top):
    assert order == ['mid subpackage', 'innermost subpackage', 'top']
