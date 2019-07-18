#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-14 16:48
# @Author  : 冯佳欣
# @File    : 24. Swap Nodes in Pairs.py
# @Desc    :
'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        由于如果交换前两个节点，那么头节点变化，引入一个辅助节点，是的prev.next = head
        '''
        if not head or not head.next:
            return head

        prev_node = ListNode(0)
        prev_node.next = head
        head = prev_node
        while head.next and head.next.next:
            n1, n2 = head.next, head.next.next
            n1.next = n2.next
            n2.next = n1
            head.next = n2
            head = n1
        return prev_node.next
        while curr_node and curr_node.next:
            next_node = curr_node.next
            curr_node.next = next_node.next
            next_node.next = curr_node
            curr_node = curr_node.next
        return prev_node.next

        curr_node = head
        return_node = None
        # 可以交换的条件
        while curr_node and curr_node.next:
            next_node = curr_node.next
            next_curr = next_node.next


