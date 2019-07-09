'''
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0

We return the result as an array: [1, 1, 2, 3]

'''
class Solution:
    def numIslands2(self,m,n,positions):
        num = 0
        self.parent = dict()
        # 原始位置是(x,y)在新的数组中位置是x * n + y
        res_list = []
        for i in range(m * n - 1):
            self.parent[i] = i
        # 确定island
        island = [[0 for _ in range(n)] for _ in range(m)]
        # 确定相邻的四个节点坐标差值
        neibours = [(-1,0),(1,0),(0,-1),(0,1)]
        if positions:
            for pos in positions:
                num +=1
                x,y = pos[0],pos[1]
                # 分别求出相邻节点
                for nei in neibours:
                    x_nei,y_nei = x +nei[0],y +nei[1]
                    if x_nei < 0 or x_nei >= m or y_nei < 0 or y_nei >= n or island[x_nei][y_nei] == 0:
                        continue
                    pos,nei_pos = x * n + y,x_nei * n +y_nei
                    # find parent
                    while pos != self.parent[pos]:
                        pos = self.parent[pos]
                    while nei_pos != self.parent[nei_pos]:
                        nei_pos = self.parent[nei_pos]
                    # union
                    if nei_pos != pos:
                        self.parent[nei_pos] = pos
                        num -= 1
                island[x][y] = 1
                res_list.append(num)
        return res_list

if __name__ == '__main__':
    n = 3
    m = 3
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    s = Solution()
    res = s.numIslands2(m,n,positions)
    print(res)






