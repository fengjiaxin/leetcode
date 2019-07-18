#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 08:58
# @Author  : 冯佳欣
# @File    : 160. Intersection of Two Linked Lists.py
# @Desc    :
'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        '''
        思路：首先想到的是利用栈数据结构，依次放进去，然后同时抛出，最后返回最后一个相同val的节点，如果没有就是空，但是空间是o(n)
        另一种方法：
        分别计算出a,b的长度，然后可以根据长度差来判断第几个节点可能是交叉节点

        '''
        if not headA or not headB:
            return None

        def get_length(head):
            count = 1
            while head.next:
                head = head.next
                count += 1
            return count

        a_len = get_length(headA)
        b_len = get_length(headB)

        if a_len == b_len:
            while headA:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
            return None

        elif a_len > b_len:
            diff_len = a_len - b_len
            while diff_len > 0:
                headA = headA.next
                diff_len -= 1
            while headA:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
            # 跳出循环，意味这没有找到入口节点
            return None
        else:
            diff_len = b_len - a_len
            while diff_len > 0:
                headB = headB.next
                diff_len -= 1
            while headB:
                if headA == headB:
                    return headB
                else:
                    headA = headA.next
                    headB = headB.next
            return None
