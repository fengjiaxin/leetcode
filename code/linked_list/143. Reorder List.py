#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 15:43
# @Author  : 冯佳欣
# @File    : 143. Reorder List.py
# @Desc    :
'''

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        '''
        思路：首先需要确定链表的中间节点，然后将后半部分的节点存储到一个新的链表中
        最后将原先的链表和新的链表结合起来

        对于1 -> 2 -> 3 -> 4  节点来说
        首先需要先定位到2节点，然后建立dummy节点，然后将遍历后的节点插入到头节点
        变成1 -> 2 
        dummy -> 4 -> 3
        然后合并上面连个链表，变成1 -> 4 -> 2 -> 3

        对于1 -> 2 -> 3 -> 4 -> 5 链表来说
        首先需要先定位到3节点，然后建立dummy节点，然后将遍历后的节点插入头节点
        变成1 -> 2 -> 3
        dummy -> 5 -> 4
        然后合并上面的链表，变成1 -> 5 -> 2 -> 4 -> 3
        '''

        # 首先考虑边界条件
        if not head or not head.next or not head.next.next:
            return head

        def get_middle(head):
            slow = head
            fast = head
            while fast and fast.next and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # 已经将链表拆分成两部分
        middle_node = get_middle(head)
        right_half_node = middle_node.next
        middle_node.next = None

        # 将right_half 反转
        dummy = ListNode(0)
        while right_half_node:
            next_node = right_half_node.next
            right_half_node.next = dummy.next
            dummy.next = right_half_node
            right_half_node = next_node

        # 接下来需要合并链表
        curr1 = head
        curr2 = dummy.next

        while curr2:
            next_curr1 = curr1.next
            next_curr2 = curr2.next
            curr1.next = curr2
            curr2.next = next_curr1
            curr1 = next_curr1
            curr2 = next_curr2
        return head


