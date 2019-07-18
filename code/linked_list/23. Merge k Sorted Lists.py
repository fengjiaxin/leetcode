#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 21:38
# @Author  : 冯佳欣
# @File    : 23. Merge k Sorted Lists.py
# @Desc    :
'''

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        思路：核心肯定还是合并两个有序列表，但是如果合并第1，2个，然后和第3个合并，这样效率特别低
        应该采用分治方法，每次处理两个
        如果链表长度为3，首先将1和3合并，在和2合并
        如果链表长度为4，首先将1和3合并，然后2和4合并，最后1和2在合并
        '''

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # 利用递归的方法合并，返回的是排好序的头节点
        def mergeTwoLists(l1, l2):
            if not l1:
                return l2
            elif not l2:
                return l1
            else:
                if l1.val < l2.val:
                    l1.next = mergeTwoLists(l1.next, l2)
                    return l1
                else:
                    l2.next = mergeTwoLists(l1, l2.next)
                    return l2

        n = len(lists)
        while n > 1:
            k = (n + 1) // 2
            for i in range(n // 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + k])
            n = k
        return lists[0]

