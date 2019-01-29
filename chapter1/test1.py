#!user/bin/env python
# -*- coding:utf-8 -*-

"""
@author:zjh
@file:test1.py
@time:2019/01/27
"""


def is_multiple(n, m):
    bools = False
    if not isinstance(n, int) & isinstance(m, int):
        raise TypeError('n and m must be int.')
    for i in range(n + 1):
        if m * i == n:
            bools = True
            break
    return bools
