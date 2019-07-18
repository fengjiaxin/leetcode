#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 08:23
# @Author  : 冯佳欣
# @File    : 226. Invert Binary Tree.py
# @Desc    :
'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs_helper(root):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            dfs_helper(root.left)
            dfs_helper(root.right)

        if root is None:
            return root
        dfs_helper(root)
        return root
