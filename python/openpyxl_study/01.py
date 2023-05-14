# _*_ coding:utf-8 _*_
'''
@File       :01.py
@Time       :2023/4/6 23:42
@Author     :且任荣枯
@Version    :1.0

'''

import openpyxl as vb

path = './one.xlsx'
wook_book = vb.load_workbook(path)
wook_sheet = wook_book['one']
print(wook_sheet)