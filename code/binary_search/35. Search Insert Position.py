#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-13 10:00
# @Author  : 冯佳欣
# @File    : 35. Search Insert Position.py
# @Desc    :
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        思路：问题转换为找出数组中第一个>= target 的索引，需要注意的是，有可能返回len(nums)，因此采用左闭右开的方法
        '''
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) //2
            # 如果恰好找到
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        return left