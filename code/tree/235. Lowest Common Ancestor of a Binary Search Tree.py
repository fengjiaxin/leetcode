#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 07:19
# @Author  : 冯佳欣
# @File    : 235. Lowest Common Ancestor of a Binary Search Tree.py
# @Desc    :
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]




Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.


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
        思路：就是寻找两个节点的公共子节点
        我目前想到两个方法
        1.首先是分别存储从root节点到p和q的路径，分别放到栈中，然后依次弹出，弹出的第一个相等的节点就是公共祖先
        2.这是一个二叉搜索树，左 < 根 < 右，根据p和q的值可以判断p在root的节点的左边还是右边
          1.如果p和q在root的两侧，那么root一定是最低公共祖先节点
          2.如果p和q在root的一侧，那么root接续遍历，直到p和q在root的两侧
        '''
        if not root:
            return None

        def dfs_helper(node, p, q):
            # node是p和q的祖先节点情况
            if node.val == p.val or node.val == q.val or (p.val - node.val) * (q.val - node.val) < 0:
                return node
            if p.val < node.val:
                return dfs_helper(node.left, p, q)
            elif p.val > node.val:
                return dfs_helper(node.right, p, q)

        return dfs_helper(root, p, q)
