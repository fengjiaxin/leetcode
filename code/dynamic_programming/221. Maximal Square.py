#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 09:16
# @Author  : 冯佳欣
# @File    : 221. Maximal Square.py
# @Desc    :
'''

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0) and matrix[i][j] == '1':
                    dp[i][j] = 1
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                res = max(res, dp[i][j])
        return res * res

