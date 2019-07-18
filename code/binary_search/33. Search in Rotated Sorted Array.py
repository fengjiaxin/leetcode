#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-13 09:47
# @Author  : 冯佳欣
# @File    : 33. Search in Rotated Sorted Array.py
# @Desc    :

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        思路：确定范围
        对于 [0,1,2,4,5,6,7]数组，转换有两种可能行
        1,[6,7,0,1,2,4,5],其中nums[mid] = 1,可以看出mid - end 的数组是有序的，接下来需要判断target是不是在右侧数组中，如果在就二分查找，如果不在，就到左侧无序数组查找。
        2,[2,4,5,6,7,0,1],其中nums[mid] = 6，可以看出0 - mid 的数组是有序的，接下来需要判断target是不是在左侧数组，如果是就二分查护，否则去右侧无序数组查找。
        二分搜索的含义：就是每次可以去掉一半肯定不在的区间
        '''
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        if nums[right] > nums[left]:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # 右侧数组是有序的
            if nums[right] > nums[mid]:
                # target 在右侧的有序数组中
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 左侧数组是有序的
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
