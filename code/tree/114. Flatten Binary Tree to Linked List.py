#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 19:32
# @Author  : 冯佳欣
# @File    : 114. Flatten Binary Tree to Linked List.py
# @Desc    :
'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        按照 preorder的顺序进行遍历 根左右
        '''
        self.prev = None

        def inorder(root):
            if root is None:
                return

            left = root.left
            right = root.right

            root.left = None
            root.right = None
            if self.prev:
                self.prev.right = root
            self.prev = root
            # print(self.prev.val)
            inorder(left)
            inorder(right)

        inorder(root)

