# _*_ coding:utf-8 _*_
'''
@File       :conftest.py
@Time       :2023/5/15 22:25
@Author     :且任荣枯
@Version    :1.0

'''
from typing import List

def pytest_collection_modifyitems(session, config, items:List):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    items.reverse()

def pytest_addoption(parser, pluginmanager):
    mygroup = parser.getgroup("testgroup")
    mygroup.addoption("--env", # 注册一个命令行选项
                      defalut='test', # 参数的默认值
                      dest = 'env',  # 存储的变量
                      help = 'set you run env' # 帮助提示信息
    )
