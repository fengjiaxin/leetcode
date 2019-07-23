#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 14:04
# @Author  : 冯佳欣
# @File    : 215. Kth Largest Element in an Array.py
# @Desc    :
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        思路：运用快速排序的规则
        '''

        def swap(index1, index2):
            temp = nums[index1]
            nums[index1] = nums[index2]
            nums[index2] = temp

        def partion(start, end):
            if start == end:
                return start, 1
            if start < end:
                pivot = nums[end]
                index1 = start
                index2 = end
                while index1 < index2:
                    while index1 < index2 and nums[index1] <= pivot:
                        index1 += 1
                    while index1 < index2 and nums[index2] >= pivot:
                        index2 -= 1
                    swap(index1, index2)

                swap(index1, end)
                print('%d %d' % (index1, end - index1 + 1))
                return index1, end - index1 + 1

        def find_helper(start, end, k):
            index, largest = partion(start, end)
            if largest == k:
                return nums[index]
            elif largest > k:
                return find_helper(index + 1, end, k)
            else:
                return find_helper(start, index - 1, k - largest)

        return find_helper(0, len(nums) - 1, k)
