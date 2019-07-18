#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 07:16
# @Author  : 冯佳欣
# @File    : 25. Reverse Nodes in k-Group.py
# @Desc    :
'''

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
        思路：按我的理解，就是将前面k个节点进行反转
        但是需要注意的是k的长度
        '''

        def get_len(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        if not head or not head.next or k == 0:
            return head

        # 链表的长度
        n = get_len(head)
        # 链表中需要rotate几次
        rotate_time = n // k

        dummy = ListNode(0)
        tail = dummy

        # 将包含head节点的k个节点倒序插入到tail节点后面，假设1 -> 2 -> 3 -> 4,k = 3  最后变成 tail -> 3 ->2 -> 1 tail = 1,head = 4
        # 最后返回新的tail节点和head节点
        def insert_head(tail, head, k):
            new_tail = head
            for _ in range(k):
                next_node = head.next
                head.next = tail.next
                tail.next = head
                head = next_node
            return new_tail, head

        for _ in range(rotate_time):
            tail, head = insert_head(tail, head, k)
        tail.next = head
        return dummy.next



