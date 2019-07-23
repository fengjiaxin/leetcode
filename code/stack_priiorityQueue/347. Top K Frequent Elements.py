#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 20:18
# @Author  : 冯佳欣
# @File    : 347. Top K Frequent Elements.py
# @Desc    :
'''

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        思路：首先统计每个元素出现的次数
        然后用最大堆统计
        由于python 的 heapq是最小堆，可以对健值取反
        '''
        map_dict = {}
        for num in nums:
            if num not in map_dict:
                map_dict[num] = 0
            map_dict[num] += 1

        heap = []
        res = []
        for key, value in map_dict.items():
            heapq.heappush(heap, (-value, key))

        for _ in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)
        return res

