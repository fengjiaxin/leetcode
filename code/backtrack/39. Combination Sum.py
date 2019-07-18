#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 20:00
# @Author  : 冯佳欣
# @File    : 39. Combination Sum.py
# @Desc    :
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
            思路：避免重复，首先需要定义顺序，即每次只能取比本数字小的数字
            1.选择：每次可以选择比自己小的数据
            2.限制：
            3.结束， = target
        '''
        candidates.sort()
        res_list = []
        temp_list = []

        def backtrack(num, left_target):
            if left_target < 0:
                return
            if left_target == 0:
                res_list.append(temp_list.copy())
            for can in candidates:
                if can <= num:
                    temp_list.append(can)
                    backtrack(can, left_target - can)
                    temp_list.pop(-1)

        backtrack(candidates[-1], target)
        return res_list


