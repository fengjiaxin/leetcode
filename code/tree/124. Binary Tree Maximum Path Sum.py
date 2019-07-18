#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 20:11
# @Author  : 冯佳欣
# @File    : 124. Binary Tree Maximum Path Sum.py
# @Desc    :
'''

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        思路:这个题一开始居然理解有问题
        就是计算在树中的最大路径长度
        假设树结构如下所示：
                    5
                  /    \
                4        8
              /        /   \
            11       13     4
          /   \               \
         7     2               1
         对于11这个节点，有两种可能行
         1.如果11是路径的根节点，则构成路径7 - 11 -2
         2.如果11不是路径的根节点，那么对于下一部分，7 - 11 是路径的一部分

         参考答案总结的思路：
         1.与常规的path sum不同，这题的path sum可以不起始于root,也可以不终止于leaf
         2.这样的path可以归结为两种情况
          2.1 root -> leaf path中的一段，即11 -7 或 11 -2
          2.2 两个节点之间经过它们的lowest common ancestor(LCA)的path,即题目中的7 - 11 -2
         3.显然top - down 的递归不适用于该题，因为对于第2种情况，它的path sum 同时取决于LCA 左右的path_sum 的最大值
            而这样的path sum 是无法通过top - down 传递来获取的
         4.这里采用bottom - up的递归方法：
           对于节点x
           定义sub_path(x)为从x出发向leaf方向的第一类path中的最大的path sum
           定义root_path(x)为以x为LCA的第二类path中的最大path sum
           显然如果求的所有节点x的sub_path(x) 和 root_path(x),其中的最大值自然就是要求的max path sum
         5.如何求sub_path(x),root_path(x)
           5.1 sub_path(x),root_path(x)至少应该不小于x.val，因为x自己可以作为一个单节点path
           5.2 sub_path(x),root_path(x)可以从sub_path(x.left),sub_path(x.right)获取
           sub_path(x) = x.val + max(sub_path(x.left),0,sub_path(x.right))
           root_path = max(0,sub_path(x.left)) + max(0,sub_path(x.right)) + x.val

         6.可以看出root_path,sub_path 都是根据子节点的sub_path获取的，因此需要返回x节点的sub_path
         7.对于None节点，返回0





        '''
        global max_num
        max_num = float('-Inf')

        def sub_path(x):
            global max_num
            if x is None:
                return 0
            left_sub_path = sub_path(x.left)
            right_sub_path = sub_path(x.right)
            curr = x.val + max(left_sub_path, right_sub_path, 0)
            if curr > max_num:
                max_num = curr
            root_path = max(0, left_sub_path) + max(0, right_sub_path) + x.val
            if root_path > max_num:
                max_num = root_path
            return curr

        sub_path(root)
        return max_num




