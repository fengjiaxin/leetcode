#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 08:02
# @Author  : 冯佳欣
# @File    : 52. N-Queens II.py
# @Desc    :
'''

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''
class Solution:
    def __init__(self):
        self.num = 0
    def totalNQueens(self, n: int) -> int:
        temp_list = []
        def isAtack(pos,new_pos):
            x_1,y_1 = pos[0],pos[1]
            x_2,y_2 = new_pos[0],new_pos[1]
            if x_1 == x_2 or y_1 == y_2 or abs(x_1-x_2) == abs(y_1-y_2):
                return True
            return False
        def areAtack(temp_list,new_pos):
            if not temp_list:
                return False
            for pos in temp_list:
                if isAtack(pos,new_pos):
                    return True
            return False
        def backtrack(start):
            if start == n and len(temp_list)  == n:
                self.num += 1
                return
            for index_y in range(n):
                new_pos = (start,index_y)
                if not areAtack(temp_list,new_pos):
                    temp_list.append(new_pos)
                    backtrack(start + 1)
                    temp_list.pop(-1)
        backtrack(0)
        return self.num