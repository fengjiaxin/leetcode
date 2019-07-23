#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 17:13
# @Author  : 冯佳欣
# @File    : 155. Min Stack.py
# @Desc    :
'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''


class MinStack:
    '''
    思路：两个stack
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_data = []

    def push(self, x: int) -> None:
        if not self.data:
            self.data.append(x)
            self.min_data.append(x)
        else:
            self.data.append(x)
            if x >= self.min_data[-1]:
                self.min_data.append(self.min_data[-1])
            else:
                self.min_data.append(x)

    def pop(self) -> None:
        self.data.pop(-1)
        self.min_data.pop(-1)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_data[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()