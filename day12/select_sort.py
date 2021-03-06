# -*-coding:utf-8 -*-
"""
选择排序
"""
import time
import sys
import random


class Solution(object):
    def select_sort(self, s):
        """
        :type s: list
        :rtype: list
        """
        for i in range(len(s)-1):
            min = s[i]
            index = i
            for j in range(i+1, len(s)):
                if s[j] < min:
                    index = j
                    min = s[j]
            tmp = s[index]
            s[index] = s[i]
            s[i] = tmp
        return s


# a1 = [6, 5, 3, 1, 8, 7, 2, 4]
# a1 = [6, 7, 10, 7, 8, 9]
# a1 = [21, 25, 49, 25, 16, 8]
a1 = list(range(0, 10000))
random.shuffle(a1)

s = Solution()
t1 = time.time()
# for i in range(100):
str = s.select_sort(a1)
t2 = time.time()
print(t2-t1)
print(str)
