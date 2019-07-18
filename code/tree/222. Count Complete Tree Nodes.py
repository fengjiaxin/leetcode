#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 19:49
# @Author  : 冯佳欣
# @File    : 222. Count Complete Tree Nodes.py
# @Desc    :
'''

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        '''
        完全二叉树的数目，这个没有想到更好的办法，参考了一些答案，总结如下：
        求完全二叉树的节点数目，注意完全二叉树和满二叉树的唯一区别是，完全二叉树的最后一层的节点不满，而且假设最后一层有节点，都是从左边开始，这样可以得到下面两个结论
        1.加入左子树的高度等于右子树的高度，则右子树为完全二叉树，左子树为满二叉树
        2.假设高度不等，则左子树为完全二叉树，右子树为满二叉树
        3.求高度的时候只往左子树来寻找

        '''

        def get_height(root):
            height = 0
            while root:
                root = root.left
                height += 1
            return height

        if root is None:
            return 0
        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)