#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 07:31
# @Author  : 冯佳欣
# @File    : 108. Convert Sorted Array to Binary Search Tree.py
# @Desc    :
'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        思路：序列构建二叉树，可能的情况
        首先我想到的是就是每次找到中间节点，然后分别确定左右分孩子
        对于题中的例子，还有一种可能行
              0
            /   \
         -10     5
           \      \
           -3      9
        '''

        def convert_helper(start, end):
            if start == end:
                return TreeNode(nums[start])
            elif start > end:
                return None
            else:
                mid = start + (end - start) // 2
                curr = TreeNode(nums[mid])
                curr.left = convert_helper(start, mid - 1)
                curr.right = convert_helper(mid + 1, end)
                return curr

        if not nums:
            return None
        return convert_helper(0, len(nums) - 1)
