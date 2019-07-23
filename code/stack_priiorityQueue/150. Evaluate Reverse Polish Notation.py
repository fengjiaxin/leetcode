#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 17:35
# @Author  : 冯佳欣
# @File    : 150. Evaluate Reverse Polish Notation.py
# @Desc    :
'''

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        思路:维护一个运算数栈，读到运算数的时候直接进栈，而读到一个运算符的时候，从栈顶取出两个运算数，运算之后将结果作为一个运算数放回栈中，直到式子结束，辞职栈中唯一一个元素就是结果
        需要注意的是python是向下取整，因此需要注意
        '''
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop(-1)
                a = stack.pop(-1)
                if token == '+':
                    c = a + b
                elif token == '-':
                    c = a - b
                elif token == '*':
                    c = a * b
                else:
                    if a * b < 0:
                        rev_c = (-a) // b
                        c = -rev_c
                    else:
                        c = a // b
                stack.append(c)
        return stack.pop(-1)


