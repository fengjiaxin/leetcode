#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 08:23
# @Author  : 冯佳欣
# @File    : 203. Remove Linked List Elements.py
# @Desc    :
'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''
        思路：需要删除的节点可能是头节点，所以引入一个辅助节点prev_head
            除此之外，需要保留需要删除节点的前一个节点的信息
        '''
        if not head:
            return head

        prev_head = ListNode(0)
        prev_head.next = head

        prev_curr = prev_head
        curr = head
        while curr:
            next_node = curr.next
            # 需要删除curr节点，但是prev不应该动
            if curr.val == val:
                prev_curr.next = next_node
                curr.next = None
                curr = next_node
            # 不需要删除curr节点，所以prev和curr应该移动
            else:
                prev_curr = prev_curr.next
                curr = next_node
        return prev_head.next


