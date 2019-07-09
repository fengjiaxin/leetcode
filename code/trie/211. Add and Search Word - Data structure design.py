#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-09 15:00
# @Author  : 冯佳欣
# @File    : 211. Add and Search Word - Data structure design.py
# @Desc    :

'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

'''


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = -1

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if '.' not in word:
            curNode = self.root
            for c in word:
                if c not in curNode:
                    curNode[c] = {}
                curNode = curNode[c]
            curNode[self.end] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        # 这种带'.'的通配符

        def dfs(curNode, word, start_index):
            # 确定边界条件
            # 1.如果word搜索结束
            if len(word) == start_index:
                if self.end in curNode:
                    return True
                return False
            cur_str = word[start_index]
            if cur_str == '.':
                for c in curNode:
                    if c == self.end:continue
                    if dfs(curNode[c], word, start_index + 1):
                        return True
                return False
            else:
                if cur_str not in curNode:
                    return False
                return dfs(curNode[cur_str], word, start_index + 1)

        return dfs(self.root, word, 0)

if __name__ == '__main__':
    obj = WordDictionary()
    add_words = ['a','a']
    search_words = [".","a","aa","a",".a","a."]
    for aw in add_words:
        obj.addWord(aw)
    for sw in search_words:
        res = obj.search(sw)
        print(sw + '->' + str(res))