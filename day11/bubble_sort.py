# -*-coding:utf-8 -*-
"""
冒泡排序
"""
import time
import sys
import random


class Solution(object):
    def bubble_sort(self, s):
        """
        :type s: list
        :rtype: list
        """
        for i in range(1, len(s)-1):
            for j in range(len(s)-i):
                if s[j] > s[j+1]:
                    tmp = s[j+1]
                    s[j+1] = s[j]
                    s[j] = tmp
                # print(s)

        return s

# a1 = [6, 5, 3, 1, 8, 7, 2, 4]
a1 = list(range(0, 10000))
random.shuffle(a1)

s = Solution()
t1 = time.time()
# for i in range(100):
str = s.bubble_sort(a1)
t2 = time.time()
print(t2-t1)
print(str)
