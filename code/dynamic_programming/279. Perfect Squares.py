#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-21 10:09
# @Author  : 冯佳欣
# @File    : 279. Perfect Squares.py
# @Desc    :
'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution:
    def numSquares(self, n):
        '''
        思路：
        首先需要确定可能组成n的nums数组
        然后就是用动态规划进行计算
        例如n = 13
        nums = [1,4,9]
        dp(13) = 1 + min(dp(12),dp(9),dp(4))
        dp(0) = 0
        '''

        square_list = [1]
        s = 2
        while s*s<=n:
            square_list.append(s*s)
            s+=1

        dp = [i for i in range(n+1)]

        for i in range(1,n+1):
            if i in square_list:
                dp[i] = 1
            else:
                for j in square_list:
                    if j<= i:
                        dp[i] = min(dp[i],dp[j]+dp[i-j])
                    else:
                        break
        return dp[n]

