#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 07:57
# @Author  : 冯佳欣
# @File    : 19. Remove Nth Node From End of List.py
# @Desc    :
'''

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        思路：本题是移除倒数第n个节点，如果移除的是第一个节点，那么头节点会变化，因此引入一个dummy节点
        由于尾节点是倒数第1个节点，需要存储的是删除节点的前一个节点
        '''
        prev_head = ListNode(0)
        prev_head.next = head

        slow_node = prev_head
        fast_node = prev_head
        # 确定两个节点
        while n > 0:
            fast_node = fast_node.next
            n -= 1

        # 接下来需要让fast_node指向倒数第一个节点
        while fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next

        # slow_node存储的是需要删除节点的前面的一个节点
        # fast_node存储的是链表的最后一个节点

        delete_node = slow_node.next
        slow_node.next = delete_node.next

        return prev_head.next



