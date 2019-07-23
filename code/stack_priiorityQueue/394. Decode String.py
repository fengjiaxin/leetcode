#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 20:22
# @Author  : 冯佳欣
# @File    : 394. Decode String.py
# @Desc    :
'''


Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''


class Solution:
    def decodeString(self, s: str) -> str:
        '''
        思路：就是括号往stack中添加
        遇到']'就弹出
        '''
        num = 0
        stack = []
        res_str = ''
        for letter in s:
            if letter.isdigit():
                num = num * 10 + int(letter)
                continue
            else:
                if num != 0:
                    stack.append(num)
                    num = 0
                if letter not in ['[', ']']:
                    stack.append(letter)
                elif letter == '[':
                    stack.append(letter)
                elif letter == ']':
                    print(stack)
                    while stack[-1] != '[':
                        cur = stack.pop(-1)
                        res_str = cur + res_str
                        print(res_str)
                    # 将和']'对应的'['弹出
                    stack.pop(-1)
                    last_num = stack.pop(-1)
                    res_str = last_num * res_str
                    stack.append(res_str)
                    res_str = ''
        res_str = ''
        print(stack)
        for letter in stack:
            res_str += letter
        return res_str
