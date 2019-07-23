#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 16:06
# @Author  : 冯佳欣
# @File    : 136. Single Number.py
# @Desc    :
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4



'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        思路：这个题明显就是利用数字，和操作与或
        a ^ 0 = a
        a ^ a = 0
        a ^ b ^ a = a ^ a ^ b = b

        '''
        a = 0
        for num in nums:
            a ^= num
        return a
