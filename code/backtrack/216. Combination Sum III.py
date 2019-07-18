#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 20:01
# @Author  : 冯佳欣
# @File    : 216. Combination Sum III.py
# @Desc    :
'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        思路：
        1.选择：为了重复，每次只选择比自己大的
        2.限制：
        3.结束，如果剩余k == 0 and 剩余n == 0
        '''
        res_list = []
        temp_list = []
        candidates = list(range(10))

        def backtrack(start, left_k, left_n):
            if left_k == 0:
                if left_n == 0:
                    res_list.append(temp_list.copy())
                else:
                    return
            for i in range(start, 10):
                key = candidates[i]
                temp_list.append(key)
                backtrack(i + 1, left_k - 1, left_n - key)
                temp_list.pop(-1)

        backtrack(1, k, n)

        return res_list