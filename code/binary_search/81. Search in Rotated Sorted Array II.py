#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-14 10:13
# @Author  : 冯佳欣
# @File    : 81. Search in Rotated Sorted Array II.py
# @Desc    :
'''
81. Search in Rotated Sorted Array II
Medium

703

332

Favorite

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

'''


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        思路：1.需要考虑几种特殊情况：如果未旋转，如果为空
        2.如果旋转，二分搜索需要每次都去除一半的空间
        '''

        if not nums:
            return False

        # 接下来讨论旋转的情况
        else:
            nums_length = len(nums)
            left, right = 0, nums_length - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                # nums[mid] != target
                else:
                    # 右侧是排序的
                    if nums[mid] < nums[right]:
                        if nums[mid] < target and target <= nums[right]:
                            left = mid + 1
                        else:
                            right = mid - 1
                    # 左侧是排序的
                    elif nums[mid] > nums[right]:
                        if nums[left] <= target and target < nums[mid]:
                            right = mid - 1
                        else:
                            left = mid + 1
                    else:
                        right -= 1
            return False

