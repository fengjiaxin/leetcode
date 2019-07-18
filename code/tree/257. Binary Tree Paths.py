#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 08:54
# @Author  : 冯佳欣
# @File    : 257. Binary Tree Paths.py
# @Desc    :
'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        '''
        思想:还是使用回溯法
        '''
        if not root:
            return []
        res_list = []
        temp_list = []

        def dfs_helper(node):
            # 只是叶子节点
            if not node.left and not node.right:
                temp_list.append(str(node.val))
                print(temp_list)
                res_list.append(temp_list.copy())
                temp_list.pop(-1)
            else:
                if node.left:
                    temp_list.append(str(node.val))
                    print(temp_list)
                    dfs_helper(node.left)
                    temp_list.pop(-1)
                if node.right:
                    temp_list.append(str(node.val))
                    print(temp_list)
                    dfs_helper(node.right)
                    temp_list.pop(-1)

        dfs_helper(root)
        res = []
        for temp in res_list:
            res_str = '->'.join(temp)
            res.append(res_str)
        return res

