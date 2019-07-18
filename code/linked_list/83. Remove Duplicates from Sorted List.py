#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 08:10
# @Author  : 冯佳欣
# @File    : 83. Remove Duplicates from Sorted List.py
# @Desc    :
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        思路：最简单的方法，肯定是每次遍历一个节点的时候和前一个节点进行比较，如果val重复，就过去
        '''
        if not head or not head.next:
            return head

        dummy_node = ListNode(0)

        prev_node = dummy_node
        prev_val = float('Inf')

        curr = head
        while curr:
            next_node = curr.next
            if curr.val != prev_val:
                curr.next = None
                prev_node.next = curr
                prev_val = curr.val
                prev_node = prev_node.next
            curr = next_node
        return dummy_node.next



