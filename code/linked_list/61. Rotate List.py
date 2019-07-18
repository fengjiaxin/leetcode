#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 19:42
# @Author  : 冯佳欣
# @File    : 61. Rotate List.py
# @Desc    :
'''

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        思路：肯定不能每次rotate一个元素，那样太慢
        第2个例子，k = 4 转换结果和k = 1是一样的
        因此首先需要获取链表的长度
        '''

        def get_len(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        # 这几种特殊情况真的需要考虑，如果k == 0 或者k 是链表的整数倍，则相当于没有rotate
        if not head or not head.next or k == 0 or k % get_len(head) == 0:
            return head

        list_len = get_len(head)
        k = k % list_len

        dummy = ListNode(0)
        dummy.next = head

        # left_len是链表向后遍历的长度
        left_len = list_len - k
        curr = dummy
        for i in range(left_len):
            curr = curr.next
        # 此时curr需是需要转换节点的第一个节点的前一个节点
        next_node = curr.next
        curr.next = None
        curr = next_node

        # 此时curr是需要调换的第一个节点
        first = curr
        last = curr
        while last.next:
            last = last.next
        # 此时first存储的是需要转换的第一个节点，last存储的是需要转换的最后一个节点
        last.next = dummy.next
        dummy.next = first

        return dummy.next
