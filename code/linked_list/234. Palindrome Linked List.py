#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 11:09
# @Author  : 冯佳欣
# @File    : 234. Palindrome Linked List.py
# @Desc    :
'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        思路：判断是否是回文,其中最简单的方法就是放到栈里，然后依次弹出，和顺序进行比较，是否相同
        另一种方法：改写链表的结构，最后存储头节点和尾节点
        '''

        if not head or not head.next:
            return True

        slow_node = head
        fast_node = head
        while fast_node.next and fast_node.next.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        # 如果链表长度是奇数，那么slow_node指向的是中间节点，如果是偶数，slow_node指向的是第 n//2 节点

        prev_node = None
        curr_node = None
        if fast_node.next:
            # 偶数节点
            tail_node = ListNode(0)
            curr_node = slow_node.next
            slow_node.next = tail_node
            prev_node = tail_node
        else:
            curr_node = slow_node.next
            prev_node = slow_node
            prev_node.next = None

        # 此时prev_node指向的是中间节点，curr_node指向的是中间节点的后一个节点
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        # 此时prev_node指向的是链表节点的尾部节点
        while head:
            if head.val != prev_node.val:
                return False
            head = head.next
            prev_node = prev_node.next
        return True

