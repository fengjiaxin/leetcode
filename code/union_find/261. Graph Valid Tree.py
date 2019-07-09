
'''
题目：

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0]and thus will not appear together in edges.

思路：

一个图是一棵合法的树的充要条件是：
1）图的边的个数比顶点个数少1；
2）图中没有任何环。
我们将每一个顶点都初始化成为一个单独的集合，然后对于每一条边，检查它的两个顶点原来是否属于同一个集合，一旦是就说明构成了环，直接返回false；否则就将这两个顶点所属的两个集合进行合并。
'''
class Solution:
    def validTree(self,n,edges):
        if len(edges) != n-1:
            return False
        # make set
        self.parent = dict()
        for i in range(n):
            self.parent[i] = i

        # connect tree
        for edge in edges:
            x,y = edge[0],edge[1]
            # 分别找出x,y的父节点
            while x != self.parent[x]:
                x = self.parent[x]
            while y != self.parent[y]:
                y = self.parent[y]
            if x !=y:
                self.parent[y] = x
                n -= 1
        return n == 1

if __name__ == '__main__':
    n = 5
    edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    s = Solution()
    res_flag = s.validTree(n,edges2)
    print(res_flag)

