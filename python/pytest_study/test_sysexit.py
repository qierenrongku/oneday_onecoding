# _*_ coding:utf-8 _*_
'''
@File       :test_sysexit.py
@Time       :2023/5/14 16:45
@Author     :且任荣枯
@Version    :1.0

'''

import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
