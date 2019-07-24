#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 17:20
# @Author  : 冯佳欣
# @File    : 64. Minimum Path Sum.py
# @Desc    :
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        这个其实就是对路径进行赋值

        '''
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # 初始值
        # 行
        dp[0][0] = grid[0][0]
        for i in range(1, cols):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
            # 列
        for j in range(1, rows):
            dp[j][0] = grid[j][0] + dp[j - 1][0]
        print(dp)

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[rows - 1][cols - 1]
