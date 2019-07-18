#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-14 11:23
# @Author  : 冯佳欣
# @File    : 153. Find Minimum in Rotated Sorted Array.py
# @Desc    :
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        思路：每次确定最小值可能在的区间范围
        两种情况
        1.最小值在mid左侧
        2.最小值在mdi右侧
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # left 乱序
            if nums[mid] < nums[right]:
                # min 一定不再[mid+1,right]
                right = mid
            # right 乱序
            else:
                left = mid + 1
        return nums[left]




