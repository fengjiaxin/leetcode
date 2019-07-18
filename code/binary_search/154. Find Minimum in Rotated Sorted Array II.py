#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-14 11:29
# @Author  : 冯佳欣
# @File    : 154. Find Minimum in Rotated Sorted Array II.py
# @Desc    :
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?


'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        思路：还是确定min可能在哪个区间，但是由于存在nums[mid] == nums[right]的情况
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 右侧是有序的，min一定不再[mid+1,right]
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                # 右侧是乱序的
                left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1
        return nums[left]
