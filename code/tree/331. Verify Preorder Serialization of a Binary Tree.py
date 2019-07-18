#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 07:57
# @Author  : 冯佳欣
# @File    : 331. Verify Preorder Serialization of a Binary Tree.py
# @Desc    :
'''
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false

'''


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        :type preorder: str
        :rtype: bool
        """
        num_count, symbol_count = 0, 0
        preorder = preorder.split(',')

        for i in range(len(preorder) - 1):
            if preorder[i].isdigit():
                num_count += 1
            elif preorder[i] == '#':
                symbol_count += 1

            if symbol_count > num_count:
                return False

        if preorder[-1] == '#':
            symbol_count += 1
        else:
            num_count += 1

        return symbol_count == num_count + 1
