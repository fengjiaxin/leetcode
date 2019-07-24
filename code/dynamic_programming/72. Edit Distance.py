#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-21 09:59
# @Author  : 冯佳欣
# @File    : 72. Edit Distance.py
# @Desc    :
'''

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        最小编辑距离：用动态规划解决
        思路：
        使用dp[i][j]表示字符串1的0～i-1,字符串2的0～j-1的最小编辑距离
        边界情况 dp[i][0] = i,dp[0][j] = j
        对于两个字符串的子串，都能分为最后一个字符相等或者不等的情况：
        1.如果words1[i-1] == words2[j-1],则dp[i][j] = dp[i-1][j-1],也就是说当前的编辑距离和最后一个字符无关。
        2.如果words1[i-1] != words2[j-1]，则存在三种可能行：
           1.在words1[i-1]处之前插入words2[j-1],然后跳过word2[j-1],继续比较word1[i-1]和word2[j]
                    dp[i][j+1] = dp[i][j] + 1 => dp[i][j] = dp[i][j-1] + 1
           2.在words1[i-1]处删除该字符，然后继续比较words1[i]和words2[j-1]
                    dp[i+1][j] = dp[i][j] + 1 => dp[i][j] = dp[i-1][j] + 1
           3.将words1[i-1]处的字符替换成words2[j-1],然后跳过，比较words1[i+1]和words2[j+1]
                    dp[i+1][j+1] = dp[i][j] + 1 => dp[i][j] = dp[i-1][j-1] + 1

        '''
        s1_len = len(word1)
        s2_len = len(word2)

        dp = [[0 for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]
        # 边界条件
        for i in range(1, s1_len + 1):
            dp[i][0] = i
        for j in range(1, s2_len + 1):
            dp[0][j] = j

        for i in range(1, s1_len + 1):
            for j in range(1, s2_len + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[s1_len][s2_len]


