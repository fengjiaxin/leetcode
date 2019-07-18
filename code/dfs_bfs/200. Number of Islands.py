#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-11 13:56
# @Author  : 冯佳欣
# @File    : 200. Number of Islands.py
# @Desc    :

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution:
    # dfs方法，但是在测试的时候迭代深度超出范围
    def numIslands_dfs(self, grid):
        if not grid:
            return 0
        '''
        思路：该题的本质是求连通区域，怎么计算
        dfs方法，首先建立visited数组，对于一个为 ‘1’ 且未被访问过的位置，我们递归进入其上下左右位置上为 ‘1’ 的数，将其 visited 对应值赋为 true，继续进入其所有相连的邻位置，这样可以将这个连通区域所有的数找出来，并将其对应的 visited 中的值赋 true，找完相邻区域后，我们将结果 res 自增1，然后我们在继续找下一个为 ‘1’ 且未被访问过的位置，以此类推直至遍历完整个原数组即可得到最终结果
        '''
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        res = 0

        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == '0' or visited[x][y]:
                return
            visited[x][y] = True
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0'or visited[i][j]:
                    continue
                dfs(i, j)
                res += 1
        return res

    def numIslands_bfs(self, grid):
        if not grid:
            return 0
        '''
        思路：bfs
        '''
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        res = 0

        nei_pos_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                res += 1
                queue = []
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    pos = queue.pop(0)
                    for t in nei_pos_list:
                        x = pos[0] + t[0]
                        y = pos[1] + t[1]
                        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == '0' or visited[x][y]:
                            continue
                        queue.append((x, y))
                        visited[x][y] = True
        return res

if __name__ == '__main__':
    s = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    res = s.numIslands_dfs(grid)
    print(res)


