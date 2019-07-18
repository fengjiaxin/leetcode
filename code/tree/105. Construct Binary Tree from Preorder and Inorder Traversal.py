#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 20:21
# @Author  : 冯佳欣
# @File    : 105. Construct Binary Tree from Preorder and Inorder Traversal.py
# @Desc    :
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        根据前序遍历和中序遍历构建二叉树

        '''
        if not preorder or not inorder:
            return None

        # Preorder[0] is our current root.
        root = TreeNode(preorder[0])

        # We find our current root in the inorder traversal.
        ind = inorder.index(root.val)

        # We now have two subproblems.
        #
        # First, we compare the preorder of the left subtree
        # of our current root to the inorder of the left subtree.
        # Up to and including ind is the left subtree in preorder.
        left_pre = preorder[1:ind + 1]
        left_in = inorder[:ind]
        root.left = self.buildTree(left_pre, left_in)

        # We proceed similarly for the right subtree.
        right_pre = preorder[ind + 1:]
        right_in = inorder[ind + 1:]
        root.right = self.buildTree(right_pre, right_in)

        return root
