# -*-coding:utf-8 -*-
"""
堆排序
"""
import time
import sys
import random


class Solution(object):
    def bucket_sort(self, s):
        """
        桶排序
        :type s: list
        :rtype: list
        """
        bucket = [0 for _ in range(max(s)+1)]

        for i in s:
            bucket[i] += 1

        sort_s = []
        # for i in range(len(bucket)-1, -1, -1):
        for i in range(0, len(bucket)):
            for _ in range(bucket[i]):
                sort_s.append(i)
        return sort_s

# a1 = [6, 5, 3, 1, 8, 7, 2, 4]
# a1 = [21, 25, 49, 25, 16, 8]
a1 = list(range(0, 10000))
random.shuffle(a1)

s = Solution()
t1 = time.time()
for i in range(100):
    str = s.bucket_sort(a1)
t2 = time.time()
print(t2-t1)
print(str)
