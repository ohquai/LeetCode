# -*-coding:utf-8 -*-
"""
希尔排序（插入排序的一种）
"""
import time
import sys
import random


class Solution(object):
    def shell_sort(self, s, k):
        """
        :type s: list
        :rtype: list
        """
        n = len(s)
        gap = int(n / k) + 1
        while gap >= 1:
            for i in range(gap, n):
                tmp = s[i]
                if s[i] < s[i-gap]:
                    for j in range(i-gap, -1, -gap):
                        if s[j] > s[j+gap]:
                            s[j+gap] = s[j]
                            s[j] = tmp
                            # print(s)
                        else:
                            break
            if gap == 1:
                break
            else:
                gap = int(gap / k) + 1

        return s


# a1 = [6, 5, 3, 1, 8, 7, 2, 4]
# a1 = [21, 25, 49, 25, 16, 8]
a1 = list(range(0, 10000))
random.shuffle(a1)

s = Solution()
t1 = time.time()
for i in range(100):
    str = s.shell_sort(a1, 3)
t2 = time.time()
print(t2-t1)
print(str)
