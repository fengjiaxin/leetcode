#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 10:18
# @Author  : 冯佳欣
# @File    : 112. Path Sum.py
# @Desc    :
'''

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        '''
        思路：用递归的方式
        递归重要的是确定程序的出口
        '''
        if not root:
            return False

        def dfs_helper(node, left_value):
            if node and not node.left and not node.right and node.val == left_value:
                return True
            else:
                left_flag = False
                right_flag = False
                if node.left:
                    left_flag = dfs_helper(node.left, left_value - node.val)
                if node.right:
                    right_flag = dfs_helper(node.right, left_value - node.val)
                return (left_flag or right_flag)

        return dfs_helper(root, sum)

