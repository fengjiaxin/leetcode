#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 19:06
# @Author  : 冯佳欣
# @File    : 86. Partition List.py
# @Desc    :
'''

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        '''
        思路：存储两个链表
        第一个链表存储小于x的节点
        第二个链表存储大于x的节点
        '''
        if not head or not head.next:
            return head

        curr = head

        less_node = ListNode(0)
        more_node = ListNode(0)

        less_curr = less_node
        more_curr = more_node

        while curr:
            next_curr = curr.next
            if curr.val < x:
                curr.next = less_curr.next
                less_curr.next = curr
                less_curr = less_curr.next
            else:
                curr.next = more_curr.next
                more_curr.next = curr
                more_curr = more_curr.next
            curr = next_curr

        less_curr.next = more_node.next
        return less_node.next

