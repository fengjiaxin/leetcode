#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 19:56
# @Author  : 冯佳欣
# @File    : 78. Subsets.py
# @Desc    :
'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        temp_list = []
        length = len(nums)

        def backtrack(pos):
            res_list.append(temp_list.copy())
            print(str(temp_list))
            for index in range(pos, length):
                temp_list.append(nums[index])
                backtrack(index + 1)
                temp_list.pop(-1)

        backtrack(0)
        return res_list
