#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 08:13
# @Author  : 冯佳欣
# @File    : 100. Same Tree.py
# @Desc    :
'''

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs_same(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                return (p.val == q.val) and dfs_same(p.left, q.left) and dfs_same(p.right, q.right)

        return dfs_same(p, q)
