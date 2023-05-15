# _*_ coding:utf-8 _*_
'''
@File       :test_hook.py
@Time       :2023/5/15 22:19
@Author     :且任荣枯
@Version    :1.0

'''

import pytest

@pytest.mark.parametrize("name", ['张三', '李四'])
def test_name(name):
    print(name)