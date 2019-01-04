# -*-coding:utf-8 -*-
"""
折半插入排序
"""
import time
import sys
import random


class Solution(object):
    def binary_insertion_sort(self, s):
        """
        :type s: list
        :rtype: list
        """
        for i in range(len(s)):
            tmp = s[i]
            if i >= 1 and s[i] < s[i-1]:
                low = 0
                high = i - 1
                while low <= high:
                    # print('low: {0}, high: {1}'.format(low, high))
                    mid = int((low + high) / 2)
                    # print('s[i]: {0}'.format(s[i]))
                    if s[i] > s[mid]:
                        # print('low {0} -> {1}'.format(s[low], s[mid + 1]))
                        low = mid + 1
                    else:
                        # print('high {0} -> {1}'.format(s[high], s[mid - 1]))
                        high = mid - 1

                for j in range(i-1, low-1, -1):
                    s[j+1] = s[j]
                s[low] = tmp
                # print(s)

        return s

# a1 = [6, 5, 3, 1, 8, 7, 2, 4]
a1 = list(range(0, 10000))
random.shuffle(a1)

s = Solution()
t1 = time.time()
for i in range(100):
    str = s.binary_insertion_sort(a1)
t2 = time.time()
print(t2-t1)
print(str)
