# _*_ coding:utf-8 _*_
'''
@File       :test_class.py
@Time       :2023/5/14 17:37
@Author     :且任荣枯
@Version    :1.0

'''
class TestClass:
    def test_one(self):
        x = 'this'
        assert "h" in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x,'check')
