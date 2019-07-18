#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 20:00
# @Author  : 冯佳欣
# @File    : 77. Combinations.py
# @Desc    :
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
            思路：
                选择:每次只选比自己大的number
                限制:如果start > end 并且number > 0 ，不合法
                结束:没有可选的
        '''
        ans = []

        def backtrack(pre_list, start, end, number):
            if start > end and number > 0:
                return

            if number == 0:
                ans.append(pre_list)
                return

            for i in range(start, end + 1):
                copy_list = pre_list.copy()
                copy_list.append(i)
                backtrack(copy_list, i + 1, end, number - 1)

        backtrack([], 1, n, k)
        return ans
