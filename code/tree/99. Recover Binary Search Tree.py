#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 17:41
# @Author  : 冯佳欣
# @File    : 99. Recover Binary Search Tree.py
# @Desc    :
'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        这道题事先没有审题，以为重新修改树结构，然后乱序的个数也不清楚
        重新审题和看参考答案后，了解到在树中只有两个节点的顺序错误，并且不要修改树的结构，只需要修改树的val值即可
        思路：
        1.如果将一个有序数组中的两个元素进行交换，那么如何找出这两个数字
        对于数组1，2，7，4，5，6，3，8，9，如何判断哪两个元素发生交换
        在新的数组中，存在两对逆序并且相邻的数字，即7，4 和 6，3，由于一定是较小的数字换到了较大的数字的位置，较大的数字的位置换到了较小数字的位置
        所以在这两对中，可以简单的判断出:前一对的较大数和后一对的较小数发生了变换。
        当然存在一些特殊情况，最简单的就是1，2，4，3，5，6，只存在一对逆序，这是因为交换的两个数本身是相邻的。

        first = -1,second
        for i in range(n):
            if i > 0 and val[i-1] > val[i]:
                if first == -1:
                    first = i - 1
                    second = i
                else:
                    second = i
        swap(val[first],val[second])

        在二叉树上怎么解决，二叉树的中序遍历就是按照从小到大的顺序依次枚举每个元素，所以
        只需使用一次dfs,可以向数组一样访问二叉搜索树的每个元素

        '''
        # prev用于存储数组中的上一个节点
        self.prev = None
        self.first = None
        self.second = None

        def dfs(root):
            if root.left:
                dfs(root.left)
            if self.prev and self.prev.val > root.val:
                if self.first is None:
                    self.first = self.prev
                if self.first:
                    self.second = root
            self.prev = root
            if root.right:
                dfs(root.right)

        dfs(root)
        if self.first and self.second:
            temp = self.first.val
            self.first.val = self.second.val
            self.second.val = temp

