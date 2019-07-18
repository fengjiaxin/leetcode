#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 11:27
# @Author  : 冯佳欣
# @File    : 102. Binary Tree Level Order Traversal.py
# @Desc    :
'''

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        思路：这个是bfs，难点是如何区别不同层数的节点
        '''
        if not root:
            return []
        res_list = []
        global_queue = []
        global_queue.append(root)
        while global_queue:
            temp_list = []
            new_queue = []
            while global_queue:
                curr_node = global_queue.pop(0)
                temp_list.append(curr_node.val)
                if curr_node.left:
                    new_queue.append(curr_node.left)
                if curr_node.right:
                    new_queue.append(curr_node.right)
            res_list.append(temp_list.copy())
            global_queue = new_queue
        return res_list


