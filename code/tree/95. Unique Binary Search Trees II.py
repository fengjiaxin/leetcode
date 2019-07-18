#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 07:46
# @Author  : 冯佳欣
# @File    : 95. Unique Binary Search Trees II.py
# @Desc    :
'''

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        这道题首先是构建二叉树，然后由于序列是有序的，因此左边的一定是左子树，右边的一定是右子树，由于很多子结构都是重复利用的，因此可以用备忘录的动态规划算法，dict[(start,end)] 存储的是区间[start,end]范围内可以生成的所有bst的根节点的列表
        '''
        if n == 0:
            return []

        mem_dict = {}

        def helper(start, end):
            if start > end:
                return [None]
            if (start, end) in mem_dict:
                return mem_dict[(start, end)]
            res = []
            for i in range(start, end + 1):
                left = helper(start, i - 1)
                right = helper(i + 1, end)
                for a in left:
                    for b in right:
                        node = TreeNode(i)
                        node.left = a
                        node.right = b
                        res.append(node)
            mem_dict[(start, end)] = res
            return res

        return helper(1, n)

