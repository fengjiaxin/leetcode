#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 08:58
# @Author  : 冯佳欣
# @File    : 173. Binary Search Tree Iterator.py
# @Desc    :
'''

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    '''
    思路：就是中序遍历，将节点放到一个queue中，先进先出
    '''

    def __init__(self, root: TreeNode):
        self.queue = []
        self.__inorder(root)

    def __inorder(self, node):
        if not node:
            return
        if node.left:
            self.__inorder(node.left)
        self.queue.append(node)
        if node.right:
            self.__inorder(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.queue.pop(0)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.queue) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()