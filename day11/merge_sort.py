# -*-coding:utf-8 -*-
"""
归并排序
"""
import time
import sys
import random


class Solution(object):
    def merge_sort(self, s):
        """
        :type s: list
        :rtype: list
        """
        if len(s) == 1:
            return s
        else:
            left_child = self.merge_sort(s[:int(len(s)/2)])
            right_child = self.merge_sort(s[int(len(s) / 2):])

            left_index = 0
            right_index = 0
            new_s = []
            while left_index < len(left_child) and right_index < len(right_child):
                if left_child[left_index] < right_child[right_index]:
                    new_s.append(left_child[left_index])
                    left_index += 1
                else:
                    new_s.append(right_child[right_index])
                    right_index += 1
            if left_index < len(left_child):
                new_s.extend(left_child[left_index:])
            if right_index < len(right_child):
                new_s.extend(right_child[right_index:])
            return new_s


# a1 = [6, 5, 3, 1, 8, 7, 2, 4]
a1 = list(range(0, 10000))
random.shuffle(a1)

s = Solution()
t1 = time.time()
for i in range(100):
    str = s.merge_sort(a1)
t2 = time.time()
print(t2-t1)
print(str)
