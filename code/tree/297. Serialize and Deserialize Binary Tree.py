#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 15:38
# @Author  : 冯佳欣
# @File    : 297. Serialize and Deserialize Binary Tree.py
# @Desc    :
'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# class Codec:
#     '''
#     这个就是序列化存储问题
#     最简单的办法就是bfs，如果是空就存储'',个人觉得如果是一直在一边的这种情况，存储的字符串特特别大
#     因此还是通过前序遍历的字符串和中序遍历的字符串来恢复树的结构,上述有一种情况不正确，如果值相同的话，就回重复，因此这种方法不行
#     '''
#
#     # 获取前序遍历字符串
#     def _get_postorder_str(self, root):
#         res_list = []
#
#         def postorder_helper(root):
#             res_list.append(str(root.val))
#             if root.left:
#                 postorder_helper(root.left)
#             if root.right:
#                 postorder_helper(root.right)
#
#         postorder_helper(root)
#         return ','.join(res_list)
#
#     # 获取中序遍历字符串
#     def _get_inorder_str(self, root):
#         res_list = []
#
#         def inorder_helper(root):
#             if root.left:
#                 inorder_helper(root.left)
#             res_list.append(str(root.val))
#             if root.right:
#                 inorder_helper(root.right)
#
#         inorder_helper(root)
#         return ','.join(res_list)
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#         if root is None:
#             return ''
#         post_str = self._get_postorder_str(root)
#         in_str = self._get_inorder_str(root)
#         return post_str + ':' + in_str
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype: TreeNode
#         """
#         if data == '':
#             return None
#         print(data)
#         vec = data.split(':')
#         post_list = vec[0].split(',')
#         in_list = vec[1].split(',')
#
#         length = len(post_list)
#
#         def restruct_tree(post_start, post_end, in_start, in_end):
#             # print('%d %d %d %d'%(post_start,post_end,in_start,in_end))
#             if post_start > post_end or in_start > in_end:
#                 return None
#             if in_start == in_end and post_start == post_end:
#                 return TreeNode(int(post_list[post_start]))
#
#             val_str = post_list[post_start]
#             root = TreeNode(int(val_str))
#             pos_root_index = in_list.index(val_str) - post_start
#
#             root.left = restruct_tree(post_start + 1, post_start + pos_root_index, in_start,
#                                       in_start + pos_root_index - 1)
#             root.right = restruct_tree(post_start + pos_root_index + 1, post_end, pos_root_index + 1, in_end)
#             return root
#
#         return restruct_tree(0, length - 1, 0, length - 1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    这个就是序列化存储问题
    最简单的办法就是bfs，如果是空就存储'',个人觉得如果是一直在一边的这种情况，存储的字符串特特别大
    因此还是通过前序遍历的字符串和中序遍历的字符串来恢复树的结构,上述有一种情况不正确，如果值相同的话，就回重复，因此这种方法不行
    '''

    # 获取前序遍历字符串
    def _get_postorder_str(self, root):
        res_list = []

        def postorder_helper(root):
            res_list.append(str(root.val))
            if root.left:
                postorder_helper(root.left)
            if root.right:
                postorder_helper(root.right)

        postorder_helper(root)
        return ','.join(res_list)

    # 获取中序遍历字符串
    def _get_inorder_str(self, root):
        res_list = []

        def inorder_helper(root):
            if root.left:
                inorder_helper(root.left)
            res_list.append(str(root.val))
            if root.right:
                inorder_helper(root.right)

        inorder_helper(root)
        return ','.join(res_list)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        res_list = []
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node:
                res_list.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res_list.append('nan')
        return ' '.join(res_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None

        res_list = data.split()
        root = TreeNode(int(res_list.pop(0)))
        queue = []
        queue.append(root)
        while res_list:
            cur = queue.pop(0)
            tmp = res_list.pop(0)
            if tmp != 'nan':
                cur.left = TreeNode(int(tmp))
                queue.append(cur.left)
            if not res_list:
                return root
            tmp = res_list.pop(0)
            if tmp != 'nan':
                cur.right = TreeNode(int(tmp))
                queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))