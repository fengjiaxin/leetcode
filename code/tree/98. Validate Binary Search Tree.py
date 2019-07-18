#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 08:06
# @Author  : 冯佳欣
# @File    : 98. Validate Binary Search Tree.py
# @Desc    :
'''

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        思路：怎么判断一个二叉搜索树是不是有效的
        一个最简单的方法就是中序遍历，可以获取一个序列，如果这个序列是严格递增的，那么就是有序的
        另一个办法就是分别递归的判断子树是不是有效的，同时还要保证右子树的最小值要大于该节点，左子树的最大值要小于该节点
        '''

        def get_min(node):
            if node:
                while node.left:
                    node = node.left
                return node.val

        def get_max(node):
            if node:
                while node.right:
                    node = node.right
                return node.val

        def valid_helper(node):
            # 空节点
            if node is None:
                return True
            if node.left:
                if node.left.val >= node.val or get_max(node.left) >= node.val:
                    return False
            if node.right:
                if node.right.val <= node.val or get_min(node.right) <= node.val:
                    return False
            # 还要判断子节点
            return valid_helper(node.left) and valid_helper(node.right)

        return valid_helper(root)

