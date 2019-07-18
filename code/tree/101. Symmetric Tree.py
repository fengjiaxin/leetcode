#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 08:20
# @Author  : 冯佳欣
# @File    : 101. Symmetric Tree.py
# @Desc    :
'''

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs_helper(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                if p.val != q.val:
                    return False
                else:
                    return dfs_helper(p.left, q.right) and dfs_helper(p.right, q.left)

        if root is None:
            return True
        return dfs_helper(root.left, root.right)
