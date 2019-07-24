#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 16:35
# @Author  : 冯佳欣
# @File    : 120. Triangle.py
# @Desc    :
'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        这个是杨辉三角，下一行比上一行多一个元素
        对于一个data[i][j]，和它相邻的元素是data[i+1][j] 和 data[i+1][j+1],假设用min[i][j]表示从第i行第j列处的数字开始往下到最后一层的最小路径和
        min[i][j] = data[i][j] + min(min[i+1][j],min[i+1][j+1])

        但是上述需要空间O(n * n)
        可以从下往上求解最小路径和
        '''
        max_num = len(triangle[-1])
        dp = triangle[-1].copy()

        for i in range(max_num - 2, -1, -1):
            for j in range(0, i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]

