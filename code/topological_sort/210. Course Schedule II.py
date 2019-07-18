#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 17:35
# @Author  : 冯佳欣
# @File    : 210. Course Schedule II.py
# @Desc    :

'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .


'''


class Solution:
    def findOrder(self, numCourses, prerequisites):
        '''
        思路：利用dfs来进行拓扑排序
        '''
        # 定义全局变量
        self.white = 1
        self.gray = 2
        self.black = 3
        graph = dict()
        for i in range(numCourses):
            graph[i] = []

        for desc, src in prerequisites:
            graph[src].append(desc)

        res_list = []
        self.is_possible = True
        visited = [self.white for _ in range(numCourses)]

        def dfs(vertex):
            if not self.is_possible:
                return
            visited[vertex] = self.gray
            for u in graph[vertex]:
                if visited[u] == self.white:
                    dfs(u)
                elif visited[u] == self.gray:
                    self.is_possible = False
            visited[vertex] = self.black
            res_list.append(vertex)

        for ver in range(numCourses):
            if visited[ver] == self.white:
                dfs(ver)

        if self.is_possible:
            return res_list[::-1]
        else:
            return []
