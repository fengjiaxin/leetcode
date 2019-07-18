#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 20:03
# @Author  : 冯佳欣
# @File    : 60. Permutation Sequence.py
# @Desc    :
'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

'''
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 存储阶层
        factorial_list = []
        for i in range(0,n):
            factorial_list.append(math.factorial(i))

        pre_str_list = []

        def backtrack(left_num_list,k):
            if len(left_num_list) == 0:
                return
            length = len(left_num_list)
            fac_val = factorial_list[length-1]
            pick_index = (k-1)// fac_val
            pre_str_list.append(str(left_num_list[pick_index]))
            k = k % fac_val
            left_num_list.pop(pick_index)
            backtrack(left_num_list,k)

        backtrack(list(range(1, n + 1)), k)
        return "".join(pre_str_list)