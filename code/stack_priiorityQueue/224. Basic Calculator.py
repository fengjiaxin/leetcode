#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-24 10:26
# @Author  : 冯佳欣
# @File    : 224. Basic Calculator.py
# @Desc    :
'''

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''


class Solution:
    def calculate(self, s: str) -> int:
        '''
        思路：使用res表示不包括栈里数字在内的结果，num表示当前操作的数字，sign表示运算符的符号，用栈保存晕倒括号时前面计算好了的结果和运算符。
        1.如果当前是数字，那么更新计算当前数字
        2.如果当前是操作符号，那么需要更新计算当前计算的结果res，并把num,sign重新设置
        3.如果当前是(,那么说明后面的小括号里的内容需要优先计算，所以把res,sign进栈，更新res,sign重新设置
        4.如果当前是），说明当前括号里的内容已经计算完毕，所以要把之前的结果出栈，然后计算整个式子的结果

        '''

        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res = res + sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res = res + sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign * num
        return res
