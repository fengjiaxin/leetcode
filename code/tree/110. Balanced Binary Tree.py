#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 12:39
# @Author  : 冯佳欣
# @File    : 110. Balanced Binary Tree.py
# @Desc    :
'''

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        '''
        思路：判断每个节点是否平衡，首先需要获取节点的最大深度
        '''

        def get_depth(node):
            if node is None:
                return 0
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            return max(left_depth, right_depth) + 1

        def dfs_balance(node):
            if not node:
                return True
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            if abs(left_depth - right_depth) > 1:
                return False
            return dfs_balance(node.left) and dfs_balance(node.right)

        return dfs_balance(root)

