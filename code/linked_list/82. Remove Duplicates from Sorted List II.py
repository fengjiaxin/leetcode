#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 08:42
# @Author  : 冯佳欣
# @File    : 82. Remove Duplicates from Sorted List II.py
# @Desc    :
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        思路：给定的是一个有序的链表，删除重复的节点
        由于需要删除的可能是第一个节点，所以引入一个辅助节点prev_head
        '''
        if not head or not head.next:
            return head

        prev_head = ListNode(0)
        prev_head.next = head

        prev_curr = prev_head

        # 找出value相同的first节点和last节点
        first_node = head
        last_node = first_node
        while first_node:
            curr_val = first_node.val
            while last_node.next:
                if last_node.next.val == curr_val:
                    last_node = last_node.next
                else:
                    break
            if first_node == last_node:
                prev_curr.next = first_node
                prev_curr = prev_curr.next
                first_node = first_node.next
                last_node = last_node.next
            else:
                first_node = last_node.next
                last_node = first_node
        # 跳出循环，此时需要给prev_curr.next赋值
        prev_curr.next = None
        return prev_head.next


