#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 14:55
# @Author  : 冯佳欣
# @File    : 142. Linked List Cycle II.py
# @Desc    :
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        思路：还是用两个指针，快慢指针来计算
        假设环的长度为c,链表的入口节点为s,链表到达s节点之前的路程为l,假设在m点处相遇，m距离s的长度为k,假设经过x步相遇。那么短路程长度为
        short_len = x = l + k
        long_len = 2x = l + k + nc 其中n>0

        根据上式能够推出 l = n * c - k

        注意n * c -k 可以拆分出(n-1) * c + c-k
        其中c -k 代表环中m节点到s节点的剩余距离

        也就是说在m节点处，在走 l = n * c - k 步，可以到达s节点
        其中长度l正好是从head节点到达s节点的路径

        接下来将slow节点放到head处，接下来fast/slow节点分别每次只移动一个位置，然后会在s节点相遇        
        '''
        if not head or not head.next or not head.next.next:
            return None
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # 判断是因为什么跳出循环的
        if slow != fast:
            return None
        else:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
