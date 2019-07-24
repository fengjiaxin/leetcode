#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 16:14
# @Author  : 冯佳欣
# @File    : 63. Unique Paths II.py
# @Desc    :
'''

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        思路：如果在边界处遇到1，之后的初始状态为0

        如果在中间某处遇到1，其中设置为0
        '''
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp_list = [[0 for _ in range(cols)] for _ in range(rows)]
        # 设置第一行
        for i in range(cols):
            if obstacleGrid[0][i] == 0:
                dp_list[0][i] = 1
            else:
                break
        # 设置第一列
        for i in range(rows):
            if obstacleGrid[i][0] == 0:
                dp_list[i][0] = 1
            else:
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] != 1:
                    dp_list[i][j] = dp_list[i - 1][j] + dp_list[i][j - 1]
        return dp_list[rows - 1][cols - 1]