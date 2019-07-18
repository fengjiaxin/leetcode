#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-14 11:45
# @Author  : 冯佳欣
# @File    : 349. Intersection of Two Arrays.py
# @Desc    :
'''

compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        思路：
        1.首先将其中一个数组排序
        2.然后从该排序数组中，利用二分搜索法查找给定的元素是否在该数组中
        '''
        if not nums1 or not nums2:
            return []
        nums1.sort()

        # print(nums1)

        def isExists(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
            if left == len(nums):
                return False
            else:
                if nums[left] == target:
                    return True
                else:
                    return False

        res_set = set()
        for key in nums2:
            if isExists(nums1, key):
                res_set.add(key)
        return list(res_set)


