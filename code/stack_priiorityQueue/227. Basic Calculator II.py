#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 19:49
# @Author  : 冯佳欣
# @File    : 227. Basic Calculator II.py
# @Desc    :
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

'''


class Solution:
    def calculate(self, s: str) -> int:
        '''
        思路：有优先级
        先乘除，后加减

        如果是乘法或者除法，需要用前面的数和当前的数做运算，因此可以用栈来记录前面的数字，用一个符号变量记录前一个符号，当遍历到一个新的数字时，判断一下前面的符号是什么，如果是乘除，就和前面的数字运算，如果是+，就向栈中push这个数字，如果是-，就push这个数字的负数，遍历到结尾，把最后一个数字入栈，此时栈中存放的都是要进行加法运算的数字
        '''
        stack = []
        # 首先先把数字取出来
        num_str = ''
        operators = ['+', '-', '*', '/']
        for letter in s:
            if letter is ' ':
                continue
            elif letter in operators:
                num_str += ' ' + letter + ' '
            else:
                num_str += letter

        str_list = num_str.split(' ')
        print(str_list)
        op = '+'
        for letter in str_list:
            # 是数字
            if letter not in operators:
                if op == '+':
                    stack.append(int(letter))
                elif op == '-':
                    stack.append(-int(letter))
                elif op == '*':
                    a = stack.pop(-1)
                    stack.append(a * int(letter))
                elif op == '/':
                    a = stack.pop(-1)
                    if a * int(letter) < 0:
                        stack.append(-((-a) // int(letter)))
                    else:
                        stack.append(a // int(letter))
            else:
                op = letter

        res_num = 0
        for num in stack:
            res_num += num
        return res_num


