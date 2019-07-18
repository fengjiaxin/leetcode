#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 20:24
# @Author  : 冯佳欣
# @File    : 107. Binary Tree Level Order Traversal II.py
# @Desc    :
'''

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res_list = []
        global_queue = []
        global_queue.append(root)
        while global_queue:
            temp_list = []
            new_queue = []
            while global_queue:
                node = global_queue.pop(0)
                temp_list.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            global_queue = new_queue
            res_list.insert(0, temp_list.copy())
        return res_list

