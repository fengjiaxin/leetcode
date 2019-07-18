#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 14:01
# @Author  : 冯佳欣
# @File    : 116. Populating Next Right Pointers in Each Node.py
# @Desc    :
'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example:
Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.


'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        思路：还是bfs
        '''
        if not root:
            return None
        global_queue = []
        global_queue.append(root)

        while global_queue:
            new_queue = []
            # 增加next
            for i in range(len(global_queue) - 1):
                global_queue[i].next = global_queue[i + 1]
            global_queue[-1].next = None
            while global_queue:
                node = global_queue.pop(0)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            global_queue = new_queue
        return root

