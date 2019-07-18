#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 07:29
# @Author  : 冯佳欣
# @File    : 92. Reverse Linked List II.py
# @Desc    :
'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        '''
        思路：如果m == 1的话，链表的头节点会变化，可以添加一个辅助节点
        另一个辅助节点负责reverse链表
        '''
        if m == n or not head or not head.next:
            return head

        prev_head = ListNode(0)
        prev_head.next = head

        # 存储反转链表的辅助头节点
        temp_node = ListNode(0)
        # 存储反转链表的辅助tail节点

        tail_node = None
        curr = prev_head
        # 此时curr记录的是m的前一个节点

        length = n - m + 1
        while m > 1:
            curr = curr.next
            m -= 1

        # 将m-n的链表进行翻转，并保存在temp_node.next中
        while length > 0:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = temp_node.next
            temp_node.next = next_node
            if not tail_node:
                tail_node = next_node
            length -= 1

        curr_next_node = curr.next
        curr.next = temp_node.next
        tail_node.next = curr_next_node
        return prev_head.next

