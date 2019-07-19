#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 11:42
# @Author  : 冯佳欣
# @File    : 93. Restore IP Addresses.py
# @Desc    :
'''

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        思路：代码还是自己写吧
        一个有效的IP地址由4个数字组成，每个数字在0-255之间。对于其中的2位数或3位数，不能以0开头。所以对于以s[i]开头的数字有3种可能：
        1. s[i]
        2. s[i : i+1]，s[i] !=0时
        3. s[i : i+2]，s[i] != 0，且s[i : i+2] <= 255

        '''
        temp_list = []
        res_list = set()

        def backtrack(leave_str, leave_num):
            print(leave_str)
            if leave_str == '' and leave_num == 0:
                res_list.add('.'.join(temp_list))
                return
            elif (leave_str == '' and leave_num > 0) or (leave_str != '' and leave_num == 0):
                return
            else:
                # 单个长度
                for l in range(1, 4):
                    if l - 1 > len(leave_str):
                        break
                    if isvalid(leave_str[0:l]):
                        temp_list.append(leave_str[0:l])
                        backtrack(leave_str[l:], leave_num - 1)
                        temp_list.pop(-1)

        def isvalid(num_str):
            if num_str == '' or int(num_str) > 255:
                return False
            elif len(num_str) >= 2 and num_str[0] == '0':
                return False
            return True

        backtrack(s, 4)
        return list(res_list)

