# _*_ coding:utf-8 _*_
'''
@File       :conftest.py
@Time       :2023/5/15 21:53
@Author     :且任荣枯
@Version    :1.0

'''
def pytest_runtest_setup(item):
    print('setting up', item)

