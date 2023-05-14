# _*_ coding:utf-8 _*_
'''
@File       :myinvoke.py
@Time       :2023/5/14 18:35
@Author     :且任荣枯
@Version    :1.0

'''
import sys
import  pytest

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run report finishing")


if __name__== "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))