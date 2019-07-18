#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 08:06
# @Author  : 冯佳欣
# @File    : 111. Minimum Depth of Binary Tree.py
# @Desc    :
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        思路：这个肯定是用递归的方式
        '''

        def get_depth(node):
            if node is None:
                return 0
            elif node and not node.left and not node.right:
                return 1
            else:
                min_depth = float('Inf')
                if node.left:
                    left_depth = get_depth(node.left)
                    if left_depth < min_depth:
                        min_depth = left_depth
                if node.right:
                    right_depth = get_depth(node.right)
                    if right_depth < min_depth:
                        min_depth = right_depth
                return min_depth + 1

        return get_depth(root)
