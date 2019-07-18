#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 08:01
# @Author  : 冯佳欣
# @File    : 51. N-Queens.py
# @Desc    :
'''

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res_list = []
        temp_list = []

        # 判断两个位置是否可攻击
        def isAtack(pos1, pos2):
            x_1, y_1 = pos1[0], pos1[1]
            x_2, y_2 = pos2[0], pos2[1]
            if x_1 == x_2 or y_1 == y_2 or (abs(x_1 - x_2) == abs(y_1 - y_2)):
                return True
            return False

        def areAtack(temp_list, new_pos):
            if not temp_list:
                return False
            for pos in temp_list:
                if isAtack(pos, new_pos):
                    return True
            return False

        def pos2str(pos):
            res_str_list = ['.' for _ in range(n)]
            res_str_list[pos[1]] = 'Q'
            return ''.join(res_str_list)

        def temp2str(temp_list):
            res = []
            for pos in temp_list:
                res.append(pos2str(pos))
            return res

        def backtrack(start):
            if start == n:
                if len(temp_list) == n:
                    res_list.append(temp2str(temp_list))
                    return
            for index_y in range(n):
                new_pos = (start, index_y)
                if not areAtack(temp_list, new_pos):
                    temp_list.append(new_pos)
                    backtrack(start + 1)
                    temp_list.pop(-1)

        backtrack(0)
        return res_list





