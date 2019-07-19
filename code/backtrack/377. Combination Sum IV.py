#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 10:18
# @Author  : 冯佳欣
# @File    : 377. Combination Sum IV.py
# @Desc    :
'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''
from collections import defaultdict


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        思路：回溯法，确定程序空间，同时确定出口
        1.选择：每次可以选择每个数
        2.条件，如果left_target < 0:直接结束了
        3.结束：如果left_target == 0:说明是个可行解

        # 注意只用backtrack会超时，那怎么办，用动态规划存储中间的值
        需要用一个中间数组dp来，dp[i]表示target == i的解的个数，然后从1开始遍历到target,对于每一个数i，遍历数组nums,如果i >= x
        dp[i] += dp[i-x],例如对于nums = [1,2,3]的数组，target = 4,在计算dp[3]的时候，3 可以拆分成 1+ dp[2],2 + dp[1],3 + dp[0]

        如果target 大于数组中的大多数数时，可以对数组进行排序，对于数组中 > target的元素，可以直接break
        '''
        if not nums:
            return 0

        dp = defaultdict(int)
        dp[0] = 1
        # 确定初始条件dp[0],对于nums = [1,2,3],target= 1的话，dp[1] += dp[0] = 1,所以dp[0] = 1
        nums.sort()
        for i in range(1, target + 1):
            for num in nums:
                if i < num:
                    break
                dp[i] += dp[i - num]

        return dp[target]


