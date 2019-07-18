#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-12 09:58
# @Author  : 冯佳欣
# @File    : 130. Surrounded Regions.py
# @Desc    :
'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        思路：就是类似的，如果都被x包围，o变成x，但是o如果在边缘，就不是被包围
        如果直接从O开始搜索判断是不是可以到达边界，会比较麻烦，因为需要保存路径上的每个O,如果到达边界就放弃片区域，否则将其变成x
        一种聪明的做法是从四个边界出发，用dfs算法将边界开始的O区域变成另外一个临时值，这样剩下的O就是被包围的，然后将其变成为x，
        在将临时的值变为O即可。
        '''
        if not board: return
        rows = len(board)
        cols = len(board[0])

        ## 还是使用广度优先搜索bfs
        queue = []

        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    if board[i][j] == 'O':
                        board[i][j] = 'I'
                        queue.append((i, j))
                        while queue:
                            pos = queue.pop(0)
                            x, y = pos[0], pos[1]
                            if 0 <= x - 1:
                                if board[x - 1][y] == 'O':
                                    board[x - 1][y] = 'I'
                                    queue.append((x - 1, y))
                            if x + 1 <= rows - 1:
                                if board[x + 1][y] == 'O':
                                    board[x + 1][y] = 'I'
                                    queue.append((x + 1, y))
                            if 0 <= y - 1:
                                if board[x][y - 1] == 'O':
                                    board[x][y - 1] = 'I'
                                    queue.append((x, y - 1))
                            if y + 1 <= cols - 1:
                                if board[x][y + 1] == 'O':
                                    board[x][y + 1] = 'I'
                                    queue.append((x, y + 1))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'I':
                    board[i][j] = 'O'

