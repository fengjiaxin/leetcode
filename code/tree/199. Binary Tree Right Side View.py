#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 09:06
# @Author  : 冯佳欣
# @File    : 199. Binary Tree Right Side View.py
# @Desc    :
'''

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        思路：就是bfs，但是存储每层的最后一个节点
        '''
        if not root:
            return []
        global_queue = []
        res_list = []
        global_queue.append(root)
        while global_queue:
            temp_list = []
            new_queue = []
            while global_queue:
                node = global_queue.pop(0)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                temp_list.append(node.val)
            res_list.append(temp_list[-1])
            global_queue = new_queue
        return res_list
