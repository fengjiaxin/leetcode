#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-14 12:41
# @Author  : 冯佳欣
# @File    : 206. Reverse Linked List.py
# @Desc    :
'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        思路：由于反转链表的所有节点，头节点也变换，因此添加一个辅助节点dummy
        每次遍历链表，将节点插入到dummy的next
        最后返回dummy.next
        '''
        if not head or not head.next:
            return head
        prev_head = ListNode(0)
        while head:
            next_node = head.next
            head.next = prev_head.next
            prev_head.next = head
            head = next_node
        return prev_head.next

