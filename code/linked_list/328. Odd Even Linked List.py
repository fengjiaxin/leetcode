#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-14 21:26
# @Author  : 冯佳欣
# @File    : 328. Odd Even Linked List.py
# @Desc    :
'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 思路就是建立两个辅助链表，其中一个是偶数，另一个是奇数
        # 奇数
        prev_odd_node = ListNode(0)
        # 偶数
        prev_even_node = ListNode(0)
        prev_odd_node = ListNode(0)

        even_curr = prev_even_node
        odd_curr = prev_odd_node
        curr = head
        while curr and curr.next:
            n1, n2 = curr, curr.next
            curr = n2.next
            n1.next = None
            n2.next = None
            even_curr.next = n1
            odd_curr.next = n2
            even_curr = n1
            odd_curr = n2

        if curr:
            even_curr.next = curr
            even_curr = curr

        # 连接链表
        even_curr.next = prev_odd_node.next
        return prev_even_node.next

