#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 09:07
# @Author  : 冯佳欣
# @File    : 2. Add Two Numbers.py
# @Desc    :
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        思路：这个就是需要记录进位
        需要注意链表长短不一致的问题
        '''
        if not l1:
            return l2
        if not l2:
            return l1

        prev_head = ListNode(0)
        prev_curr = prev_head
        # 进位标志
        add_flag = 0

        while l1 or l2:
            curr_val = add_flag
            if l1:
                curr_val += l1.val
                l1 = l1.next
            if l2:
                curr_val += l2.val
                l2 = l2.next
            add_flag = curr_val // 10
            curr_val = curr_val % 10
            prev_curr.next = ListNode(curr_val)
            prev_curr = prev_curr.next
        # 需要判断进位是否需要新添加一位
        if add_flag:
            prev_curr.next = ListNode(1)
        return prev_head.next
