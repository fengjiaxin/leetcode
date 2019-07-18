#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 07:17
# @Author  : 冯佳欣
# @File    : 106. Construct Binary Tree from Inorder and Postorder Traversal.py
# @Desc    :
'''

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build_tree_recursive(inorder, postorder)

    def build_tree_recursive(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        left_inorder = inorder[:root_index]
        left_postorder = postorder[:len(left_inorder)]

        right_postorder = postorder[len(left_postorder):] if len(left_postorder) < len(postorder) else []
        right_inorder = inorder[-len(right_postorder):] if len(right_postorder) > 0 else []

        left = self.build_tree_recursive(left_inorder, left_postorder)
        right = self.build_tree_recursive(right_inorder, right_postorder)
        root.left = left
        root.right = right
        return root

