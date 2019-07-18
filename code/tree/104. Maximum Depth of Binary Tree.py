#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 11:38
# @Author  : 冯佳欣
# @File    : 104. Maximum Depth of Binary Tree.py
# @Desc    :
'''

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs_depth(node):
            if node is None:
                return 0
            left_depth = dfs_depth(node.left)
            right_depth = dfs_depth(node.right)
            return max(left_depth, right_depth) + 1

        return dfs_depth(root)
