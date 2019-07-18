#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-12 11:10
# @Author  : 冯佳欣
# @File    : 127. Word Ladder.py
# @Desc    :

'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        '''
        思路：想到的是bfs，每次改变一个letter，但是有很多中间状态，中间状态应该怎么保存
        hit = *it,h*t,hi*
        首先遍历给定的词表，遍历单词，然后给定的中间状态列表包含单词
        '''
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        word_length = len(beginWord)
        hidden_state_dict = dict()
        for word in wordList:
            for i in range(word_length):
                hidden_word = word[:i] + '*' + word[i + 1:]
                if hidden_word not in hidden_state_dict:
                    hidden_state_dict[hidden_word] = []
                hidden_state_dict[hidden_word].append(word)

        queue = []
        queue.append((beginWord, 1))
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(word_length):
                inter_word = current_word[:i] + '*' + current_word[i + 1:]
                if inter_word in hidden_state_dict:
                    for word in hidden_state_dict[inter_word]:
                        if word == endWord:
                            return level + 1
                        if word not in visited:
                            visited[word] = True
                            queue.append((word, level + 1))
        return 0