#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 10:58
# @Author  : 冯佳欣
# @File    : 94. Binary Tree Inorder Traversal.py
# @Desc    :
'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        思路：中序遍历:左根右
        '''
        if not root:
            return []
        res_list = []

        def dfs_inorder(node):
            if node.left:
                dfs_inorder(node.left)
            if node:
                res_list.append(node.val)
            if node.right:
                dfs_inorder(node.right)

        dfs_inorder(root)
        return res_list
