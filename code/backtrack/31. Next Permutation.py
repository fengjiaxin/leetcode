#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 10:44
# @Author  : 冯佳欣
# @File    : 31. Next Permutation.py
# @Desc    :
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        思路：下一个最大的数字，这个思想其实总是不明确，今天总结一下
        原数组
        1 2 7 4 3 1
        下一个排列是
        1 3 1 2 4 7
        如何得到的？
        观察原数组可以看出，如果从末尾往前看，数字逐渐变大，到了2时才减小，然后再从后往前找到第一个比2大的数字，3，然后交换2和3，再把此时3后面的数字转换一下即可

        '''

        # 交换元素
        def swap(i, j):
            print('%d %d' % (i, j))
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # 反转列表
        def reverse(start):

            end = len(nums) - 1
            while start < end:
                swap(start, end)
                start += 1
                end -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        print(i)
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            if j >= 0:
                swap(i, j)
        reverse(i + 1)
