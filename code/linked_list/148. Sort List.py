#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 12:37
# @Author  : 冯佳欣
# @File    : 148. Sort List.py
# @Desc    :
'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''
        这个在O(nlogn)只能是归并排序
        归并排序的算法思想如下：
        1.首先将原始问题分成两个子问题
        2.对子问题进行处理
        3.合并子问题

        很显然应该用递归的方法
        '''

        def get_middle(head):
            slow = head
            fast = head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l2:
                curr.next = l2
            elif l1:
                curr.next = l1
            else:
                curr.next = None
            return dummy.next

        def merge_sort(curr):
            if not curr or not curr.next:
                return curr
            middle_node = get_middle(curr)
            right_half = middle_node.next
            # 需要将链表断开
            middle_node.next = None
            return merge(merge_sort(curr), merge_sort(right_half))

        return merge_sort(head)



