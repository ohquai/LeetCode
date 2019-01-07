# -*-coding:utf-8 -*-
"""
堆排序
"""
import time
import sys
import random


class Solution(object):
    def __init__(self):
        self.s = []

    def heapify_desc(self, i, j):
        """
        最大堆排序
        :type i: int
        :type j: int
        :rtype: list
        """
        left_child = 2 * j + 1
        right_child = 2 * j + 2
        if right_child > len(self.s)-1-i or self.s[left_child] < self.s[right_child]:
            if self.s[j] > self.s[left_child]:
                tmp = self.s[left_child]
                self.s[left_child] = self.s[j]
                self.s[j] = tmp
        else:
            if self.s[j] > self.s[right_child]:
                tmp = self.s[right_child]
                self.s[right_child] = self.s[j]
                self.s[j] = tmp

    def heapify_asc(self, i, j):
        """
        最大堆排序
        :type i: int
        :type j: int
        :rtype: list
        """
        left_child = 2 * j + 1
        right_child = 2 * j + 2
        if right_child > len(self.s)-1-i or self.s[left_child] > self.s[right_child]:
            if self.s[j] < self.s[left_child]:
                tmp = self.s[left_child]
                self.s[left_child] = self.s[j]
                self.s[j] = tmp
        else:
            if self.s[j] < self.s[right_child]:
                tmp = self.s[right_child]
                self.s[right_child] = self.s[j]
                self.s[j] = tmp

    def heap_sort(self, s, sort='asc'):
        """
        最大堆排序
        :type s: list
        :type sort: str
        :rtype: list
        """
        self.s = s
        for i in range(len(self.s)):
            for j in range(len(self.s)-i-1, -1, -1):
                # 只找非叶子节点做heapify
                if 2 * j + 1 > len(self.s) - i - 1:
                    continue

                # 执行heapify
                if sort == 'asc':
                    self.heapify_asc(i, j)
                else:
                    self.heapify_desc(i, j)

            # 堆首与堆尾置换位置
            tmp = self.s[len(self.s)-i-1]
            self.s[len(self.s) - i - 1] = self.s[0]
            self.s[0] = tmp

        return self.s

# a1 = [6, 5, 3, 1, 8, 7, 2, 4]
# a1 = [21, 25, 49, 25, 16, 8]
a1 = list(range(0, 10000))
random.shuffle(a1)

s = Solution()
t1 = time.time()
# for i in range(100):
str = s.heap_sort(a1, sort='desc')
t2 = time.time()
print(t2-t1)
print(str)
