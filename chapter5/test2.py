#!user/bin/env python
# -*- coding:utf-8 -*-

"""
@author:zjh
@file:test2.py
@time:2019/01/28
"""

"""
    Algorithm InsertionSort(A):
        Input: An array A of n comparable elements
        Output: The array A with elements rearranged in nondecreasing order
        for k from 1 to n - 1 do 
            Insert A[k] at its proper location within A[0],A[1],...,A[k]
"""


def insertion_sort(A):
    """
    Sort list of comparable elements into nondecreasing order.

    :param A: An array of n comparable elements.
    :return: The array A with elements rearranged in nondecreasing order.
    """

    for k in range(1, len(A)):
        current_element = A[k]
        j = k
        while j > 0 and A[j - 1] > current_element:
            A[j] = A[j - 1]
            j -= 1
        A[j] = current_element
    return A
