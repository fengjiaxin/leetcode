#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 17:21
# @Author  : 冯佳欣
# @File    : 207. Course Schedule.py
# @Desc    :
'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        思路：该题主要是判断是不是有向无环图
        怎么判断该图是不是有向无环图
        '''
        # 0 代笔white 1 代表white 2 代表gray
        visited = [0 for _ in range(numCourses)]
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
        for edge in prerequisites:
            x = edge[0]
            prev = edge[1]
            graph[prev].append(x)

        def can_finish_dfs(Graph, i):
            if visited[i] == 2: return False
            if visited[i] == 1: return True
            visited[i] = 2
            for v in Graph[i]:
                if not can_finish_dfs(Graph, v):
                    return False
            visited[i] = 1
            return True

        for i in range(numCourses):
            if not can_finish_dfs(graph, i):
                return False
        return True


