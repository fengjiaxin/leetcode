#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 20:02
# @Author  : 冯佳欣
# @File    : 47. Permutations II.py
# @Desc    :
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
            由于包含重复元素,首先进行排序
            然后需要做的是剪枝，如果本次根节点的值和自己兄弟节点的根节点值值相同，需要pass
        '''
        length = len(nums)
        nums.sort()
        visited = [False for _ in range(length)]
        res = []

        def backtrack(temp_list):
            if len(temp_list) == length:
                res.append(temp_list.copy())
                return
            for index in range(length):
                if visited[index]:
                    continue
                # 如果访问过，或者和之前的数据重复
                if index > 0 and visited[index - 1] == False and nums[index] == nums[index - 1]:
                    continue
                temp_list.append(nums[index])
                visited[index] = True
                backtrack(temp_list)
                # 恢复根结点的状态
                temp_list.pop(-1)
                visited[index] = False

        backtrack([])
        return res
