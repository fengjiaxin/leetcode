#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 09:11
# @Author  : 冯佳欣
# @File    : 129. Sum Root to Leaf Numbers.py
# @Desc    :
'''

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    import math
    def sumNumbers(self, root: TreeNode) -> int:
        '''
        思路：存储所有根节点到叶子节点的的路径的值，这个肯定使用回溯法
        '''
        if not root:
            return 0
        res_list = []
        temp_list = []

        def dfs_helper(node):
            # 如果是叶子节点
            if not node.left and not node.right:
                temp_list.append(node.val)
                res_list.append(temp_list.copy())
                temp_list.pop(-1)
            if node.left:
                temp_list.append(node.val)
                dfs_helper(node.left)
                temp_list.pop(-1)
            if node.right:
                temp_list.append(node.val)
                dfs_helper(node.right)
                temp_list.pop(-1)

        dfs_helper(root)

        def get_num(num_list):
            res_num = 0
            for index, num in enumerate(num_list[::-1]):
                res_num = res_num + num * int(math.pow(10, index))
            print(num_list[::-1])
            print(res_num)
            return res_num

        res_num = 0
        for temp in res_list:
            res_num += get_num(temp)
        return res_num
