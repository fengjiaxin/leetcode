#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 15:55
# @Author  : 冯佳欣
# @File    : 62. Unique Paths.py
# @Desc    :
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        思路：可以看出每步只能往下移动或者往右移动
        所以一个坐标(x,y)的位置只能由(x-1,y)和(x,y-1)移动到
        '''
        dp_list = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp_list[i][j] = dp_list[i-1][j] + dp_list[i][j-1]
        return dp_list[m-1][n-1]