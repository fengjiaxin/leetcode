#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 16:30
# @Author  : 冯佳欣
# @File    : 318. Maximum Product of Word Lengths.py
# @Desc    :
'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''
        思路：int类型有32位，而英文小写字符只有26个，所以，对于一个字符串，把其出现过的字符放到对应的int位置上，这样每个字符串都会有一个数字摘要，如果两个字符串的摘要与之后为0，说明没有公共字符串
        '''
        ints = []
        for word in words:
            int_word = 0
            for c in word:
                int_word |= 1 << (ord(c) - ord('a'))
            ints.append(int_word)
        max_len = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if ints[i] & ints[j] == 0:
                    max_len = max(max_len,len(words[i]) * len(words[j]))
        return max_len