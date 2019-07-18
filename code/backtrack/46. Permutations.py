#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 20:02
# @Author  : 冯佳欣
# @File    : 46. Permutations.py
# @Desc    :
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            思路：
            1.选择：首先可以从剩余未处理的列表中人选一个元素
            2.限制：没有
            3.结束：当剩余列表中没有元素是，将辅助列表添加
        '''
        res = []
        length = len(nums)
        visited = [False for _ in range(length)]

        def backtrack(temp_list):
            # 先判断是否是叶子节点
            if len(temp_list) == length:
                res.append(temp_list.copy())
                return
            for i in range(len(nums)):
                if visited[i] == True:
                    continue
                temp_list.append(nums[i])
                visited[i] = True
                backtrack(temp_list)
                # 恢复状态
                temp_list.pop(-1)
                visited[i] = False

        backtrack([])
        return res
