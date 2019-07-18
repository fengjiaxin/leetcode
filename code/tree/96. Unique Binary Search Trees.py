#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 14:30
# @Author  : 冯佳欣
# @File    : 96. Unique Binary Search Trees.py
# @Desc    :
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
from collections import defaultdict


class Solution:
    def numTrees(self, n: int) -> int:
        '''
        思路：这个就是递归的计算方式
        首先总结以下边界条件
        定义函数f(n)
        f(n) = 1 n = 1
        f(n) = 2 n = 2
        f(n = 5) n = 3
        采用动态规划的备忘录机制
        '''
        mem_dict = defaultdict(lambda: None, {0: 0, 1: 1, 2: 2})

        def f(n):
            if mem_dict[n] is not None:
                return mem_dict[n]

            res = 0
            res += 2 * (mem_dict[n - 1] or f(n - 1))
            for i in range(2, n):
                res += (mem_dict[i - 1] or f(i - 1)) * (mem_dict[n - i] or f(n - i))
            mem_dict[n] = res
            return res

        return f(n)
