#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 20:01
# @Author  : 冯佳欣
# @File    : 40. Combination Sum II.py
# @Desc    :
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        思路:所有的只能用一次，因此可以引进一个visited列表，代表是否被访问
        1.选择：每次可以选择一个不重复的，并且未被访问的
        2.限制：
        3.结束：如果left_target == 0 添加到res中
        '''
        candidates.sort()
        res_list = []
        temp_list = []

        def backtrack(start, left_target):
            if left_target < 0:
                return
            if left_target == 0:
                res_list.append(temp_list.copy())
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue
                temp_list.append(candidates[index])
                backtrack(index + 1, left_target - candidates[index])
                temp_list.pop(-1)

        backtrack(0, target)
        return res_list



