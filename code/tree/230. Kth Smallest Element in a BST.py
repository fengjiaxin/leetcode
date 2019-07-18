#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 12:53
# @Author  : 冯佳欣
# @File    : 230. Kth Smallest Element in a BST.py
# @Desc    :
'''

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        最简单的办法，将中序遍历的结果存储
        '''
        res_list = []
        def inorder(root):
            if root is None:
                return
            if root.left:
                inorder(root.left)
            res_list.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return res_list[k-1]