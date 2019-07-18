#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 10:52
# @Author  : 冯佳欣
# @File    : 144. Binary Tree Preorder Traversal.py
# @Desc    :
'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]



'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        思路：前序遍历，是根左右
        '''
        if not root:
            return []

        res_list = []

        def pre_order(node):
            if node:
                res_list.append(node.val)

            if node.left:
                pre_order(node.left)

            if node.right:
                pre_order(node.right)

        pre_order(root)
        return res_list
