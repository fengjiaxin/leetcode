#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 07:40
# @Author  : 冯佳欣
# @File    : 103. Binary Tree Zigzag Level Order Traversal.py
# @Desc    :
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        思路：这个问题感觉就是bfs遍历，唯一不同的就是需要记录顺序
        count = 0
        如果count是偶数，那么从左往右遍历，否则从右往左遍历
        '''
        if not root:
            return []

        global_queue = []
        res_list = []
        global_queue.append(root)
        count = 0
        while global_queue:
            new_queue = []
            temp_list = []
            while global_queue:
                node = global_queue.pop(0)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                temp_list.append(node.val)
            if count % 2 == 0:
                res_list.append(temp_list.copy())
            else:
                res_list.append(temp_list[::-1].copy())
            count += 1
            global_queue = new_queue
        return res_list
