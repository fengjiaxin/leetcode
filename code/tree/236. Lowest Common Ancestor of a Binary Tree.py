#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 11:37
# @Author  : 冯佳欣
# @File    : 236. Lowest Common Ancestor of a Binary Tree.py
# @Desc    :
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        思路：采用dfs算法，向下深入，如果碰到p或者q，返回True,flag帮助查找是否在root的路径中找到p或者q
        '''
        global res_node
        res_node = None

        def dfs_helper(node):
            if not node:
                return False
            left = dfs_helper(node.left)
            right = dfs_helper(node.right)

            mid = node == p or node == q
            if mid + left + right >= 2:
                global res_node
                res_node = node
                print(res_node.val)
            return mid or left or right

        dfs_helper(root)
        return res_node
