#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 10:35
# @Author  : 冯佳欣
# @File    : 113. Path Sum II.py
# @Desc    :
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        '''
        思路：应该是深度优先，获得每个根节点到叶子节点的路径
        然后判断是不是符合条件
        '''
        if not root:
            return []
        res_list = []
        temp_list = []

        def dfs_helper(node, left_val):
            if node and not node.left and not node.right and node.val == left_val:
                temp_list.append(node.val)
                res_list.append(temp_list.copy())
                temp_list.pop(-1)
            if node.left:
                temp_list.append(node.val)
                dfs_helper(node.left, left_val - node.val)
                temp_list.pop(-1)
            if node.right:
                temp_list.append(node.val)
                dfs_helper(node.right, left_val - node.val)
                temp_list.pop(-1)

        dfs_helper(root, sum)
        return res_list

