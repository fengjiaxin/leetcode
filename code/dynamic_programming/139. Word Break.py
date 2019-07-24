#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-21 10:40
# @Author  : 冯佳欣
# @File    : 139. Word Break.py
# @Desc    :
'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        先说一下思路
        肯定使用动态规划，对于字符串s[:i],怎么判断是否能够拆分成符合要求的子字符串
        可以看出如果s[j:i]在字典中，并且dp[j]为True，那么dp[i] = True
        另dp[i]表示字符串s[:i]能否拆分

        '''
        str_len = len(s)
        dp = [False for _ in range(str_len + 1)]
        dp[0] = True
        for i in range(1, str_len + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

