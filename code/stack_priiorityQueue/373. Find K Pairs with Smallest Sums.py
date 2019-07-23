#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 20:03
# @Author  : 冯佳欣
# @File    : 373. Find K Pairs with Smallest Sums.py
# @Desc    :
'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

'''


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        思路：从连个数组中各取一个元素，放入到最小堆中，最小堆会调整数据结构
        首先将(nums1[i] + nums2[0],i,0) 加入堆，i的范围是（0，size1-1）
        弹出堆顶元素（sum,i,j）,将(nums1[i],nums2[j])加入到结果集合中
        若j + 1 < size2,将(nums1[i] + nums2[j+1],i,j+1)加入到堆中
        '''
        res = []
        len1, len2 = len(nums1), len(nums2)
        if not len1 or not len2:
            return res
        heap = []
        for index in range(len1):
            heapq.heappush(heap, (nums1[index] + nums2[0], index, 0))
        while len(res) < min(k, len1 * len2):
            sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
