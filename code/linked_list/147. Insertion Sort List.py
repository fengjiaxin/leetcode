#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 19:56
# @Author  : 冯佳欣
# @File    : 147. Insertion Sort List.py
# @Desc    :
'''

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

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
    def insertionSortList(self, head: ListNode) -> ListNode:
        '''
        使用插入排序，由于头节点可能变化，因此引入一个dummy节点
        插入排序是每次选出一个节点，然互将该节点插入到已经排序的节点
        '''

        if not head or not head.next:
            return head

        # 将node插入到dummy中合适的位置
        def insert(dummy, node):
            curr = dummy
            while curr and curr.val < node.val and curr.next and curr.next.val < node.val:
                curr = curr.next
            node.next = curr.next
            curr.next = node

        dummy = ListNode(float('-Inf'))

        curr = head
        while curr:
            next_node = curr.next
            insert(dummy, curr)
            curr = next_node
        return dummy.next

