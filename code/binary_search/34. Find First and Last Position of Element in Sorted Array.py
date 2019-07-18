#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-14 09:26
# @Author  : 冯佳欣
# @File    : 34. Find First and Last Position of Element in Sorted Array.py
# @Desc    :
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        思路：这个问题可以转换成两个子问题
        1，寻找nums中第一个出现target的index
        2，寻找nums中最后一个出现target的index
        '''
        if not nums:
            return [-1, -1]

        # 找出第一个>= target的下标
        def lower_bound(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return left

        def find_first(nums, target):
            left_index = lower_bound(nums, target)
            if len(nums) == left_index:
                return -1
            elif nums[left_index] != target:
                return -1
            else:
                return left_index

        def find_last(nums, target):
            right_index = lower_bound(nums, target + 1) - 1
            # 此时right_index [-1,len(nums))
            if right_index == -1:
                return -1
            elif right_index > -1:
                if nums[right_index] == target:
                    return right_index
                return -1

        return [find_first(nums, target), find_last(nums, target)]

