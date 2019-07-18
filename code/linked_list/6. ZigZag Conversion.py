#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 07:51
# @Author  : 冯佳欣
# @File    : 6. ZigZag Conversion.py
# @Desc    :
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        思路：先从数学的角度来思考，假设numRows为4
        那么第0-3个字符在第一列，第6-9个字符在第二列，这些数字怎么确定的
        首先可以确定的是，只能在中间，换言之第一行和最后一行不能填充字符，因此中间能存储的数字个数为numRows - 2
        所以字符串以竖直方式存储的起始index = n * (2 * numRows -2)
        '''
        if numRows == 1 or not s or len(s) == 1:
            return s

        def get_pos(index):
            '''
            给定index，确定index在新的模式下的坐标(x,y)
            '''
            # 一个模块能存储数字的个数
            mode_num = 2 * numRows - 2
            # 确定index在第几个模块中
            n = index // mode_num
            # 确定index在第一个模块的哪个位置
            k = index % mode_num

            x, y = 0, 0
            if k < numRows:
                x = k
                y = 0
            else:
                diff = k - (numRows - 1)
                x = (numRows - 1) - diff
                y = diff
            y += n * mode_num
            return x, y

        str_len = len(s)
        _, final_y = get_pos(str_len - 1)
        res_lists = [['' for _ in range(final_y + 1)] for _ in range(numRows)]
        for index, char in enumerate(s):
            x, y = get_pos(index)
            res_lists[x][y] = char
        res_str = ''
        for i in range(numRows):
            for j in range(final_y + 1):
                if res_lists[i][j] != '':
                    res_str += res_lists[i][j]
        return res_str


