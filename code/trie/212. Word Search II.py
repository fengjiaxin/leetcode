#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-09 16:31
# @Author  : 冯佳欣
# @File    : 212. Word Search II.py
# @Desc    :

'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

'''


class Solution:
    def make_trie(self, words):
        self.end = -1
        self.root = {}
        for word in words:
            curNode = self.root
            for letter in word:
                if letter not in curNode:
                    curNode[letter] = {}
                curNode = curNode[letter]
            curNode[self.end] = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        之前单纯采用backtrack，导致超时
        超时的情况是words特别多，其实可以用trie树的方式存储words
        '''
        self.make_trie(words)
        # 存储words中word的第一个字母在board的位置
        first_letter_dict = {}
        for word in words:
            first_letter_dict[word[0]] = []

        rows = len(board)
        cols = len(board[0])

        # 将board中符合letter的位置添加到value中
        for i in range(rows):
            for j in range(cols):
                letter = board[i][j]
                if letter in first_letter_dict:
                    first_letter_dict[letter].append((i, j))

        res_list = []

        def traverse(curNode, pos, curr, visited):
            if self.end in curNode:
                if curr not in res_list:
                    res_list.append(curr)
                # 为什么不能结束，因为trie树即使一个节点是单词，它也可能是某个单词的前缀，不能结束
            x, y = pos[0], pos[1]
            for (m, n) in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= m < rows and 0 <= n < cols and (m, n) not in visited:
                    letter = board[m][n]
                    if letter in curNode:
                        traverse(curNode[letter], (m, n), curr + letter, visited + [(m, n)])

        for letter, poss in first_letter_dict.items():
            for pos in poss:
                traverse(self.root[letter], pos, letter, [pos])
        return res_list



