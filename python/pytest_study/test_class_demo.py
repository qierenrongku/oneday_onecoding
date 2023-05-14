# _*_ coding:utf-8 _*_
'''
@File       :test_class_demo.py
@Time       :2023/5/14 17:44
@Author     :且任荣枯
@Version    :1.0

'''
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1