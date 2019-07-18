#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 19:59
# @Author  : 冯佳欣
# @File    : 90. Subsets II.py
# @Desc    :
'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        思路:针对有重复的数据
        以[1,2,2]为例子进行说明
        在处理1的子问题是，第2个2的子问题应该去掉，因为已经与第1个2的子问题重复
        那么怎么跳过重复，需要满足i > start and nums[i] == nums[i-1]
        '''
        nums.sort()
        res_list = []
        temp_list = []
        length = len(nums)

        def backtrack(start):
            res_list.append(temp_list.copy())
            print(temp_list)
            for index in range(start, length):
                if index > start and nums[index] == nums[index - 1]:
                    continue
                temp_list.append(nums[index])
                backtrack(index + 1)
                temp_list.pop(-1)

        backtrack(0)
        return res_list
