#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 15:41
# @Author  : 冯佳欣
# @File    : 70. Climbing Stairs.py
# @Desc    :
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        思路：爬楼梯，每次可爬一步或者两步
        可以看出f(n) = f(n-1) + f(n-2)
        f(1) = 1
        f(2) = 2
        '''
        if n <= 2:
            return n
        two_before = 1
        one_before = 2
        for i in range(3, n + 1):
            curr = one_before + two_before
            two_before = one_before
            one_before = curr
        return one_before
