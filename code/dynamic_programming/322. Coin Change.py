#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-21 11:22
# @Author  : 冯佳欣
# @File    : 322. Coin Change.py
# @Desc    :
'''

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        思路：就是最小组成
        题中的例子1
        dp[11] = 1 + min(dp[10],dp[9],dp[6])
        题中的例子2
        dp[3] = 1 + dp[1]
        dp[0] = -1
        关键是又一个初始值-1
        '''
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            # 硬币是1
            count = -1
            for coin in coins:
                if i >= coin and dp[i - coin] != -1:
                    curr = dp[i - coin] + 1
                    if count < 0:
                        count = curr
                    elif curr < count:
                        count = curr
            dp[i] = count
        return dp[amount]
