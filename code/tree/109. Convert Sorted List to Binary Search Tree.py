#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 08:49
# @Author  : 冯佳欣
# @File    : 109. Convert Sorted List to Binary Search Tree.py
# @Desc    :
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        思路：还是类似的，但是需要也个函数将链表拆分成两半
        '''

        # 该函数获取链表的中间节点和中间节点的前面一个节点，如果是1->2 返回None,1 如果是1- 2 -3 返回1,2,同时将左半部分断开
        def get_middle(node):
            if not node:
                return None
            slow_prev = None
            slow = node
            fast = node
            while fast.next and fast.next.next:
                slow_prev = slow
                slow = slow.next
                fast = fast.next.next
            if slow_prev:
                slow_prev.next = None
            return slow

        def convert_helper(head):
            if not head:
                return None
            mid = get_middle(head)
            print(mid.val)
            tree_node = TreeNode(mid.val)
            # 说明左侧有数据
            if head != mid:
                tree_node.left = convert_helper(head)
            right_half = mid.next
            tree_node.right = convert_helper(right_half)
            return tree_node

        return convert_helper(head)

