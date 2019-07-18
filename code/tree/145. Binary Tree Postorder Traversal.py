#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 11:02
# @Author  : 冯佳欣
# @File    : 145. Binary Tree Postorder Traversal.py
# @Desc    :
'''

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        思路：后序遍历，左右根
        '''
        if not root:
            return []
        res_list = []

        def dfs_postorder(node):
            if node.left:
                dfs_postorder(node.left)
            if node.right:
                dfs_postorder(node.right)
            res_list.append(node.val)

        dfs_postorder(root)
        return res_list
