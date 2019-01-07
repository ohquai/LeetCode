# -*-coding:utf-8 -*-
"""
快速排序
"""
import time
import sys
import random


class Solution(object):
    def quick_sort(self, s):
        """
        :type s: list
        :rtype: list
        """
        if len(s) == 1:
            return s
        else:
            h = s[-1]
            i = -1
            for j in range(len(s)-1):
                if s[j] <= h:
                    i += 1
                    tmp = s[i]
                    s[i] = s[j]
                    s[j] = tmp
                print('i: {0}, j:{1}'.format(i, j))
                print(s)
            tmp = s[i+1]
            s[i+1] = s[-1]
            s[-1] = tmp
            print('{0} epoch finish'.format(j))
            print(s)

            result = []
            if i + 1 > 0:
                result.extend(self.quick_sort(s[:i+1]))
            result.append(s[i+1])
            if i + 1 < len(s)-1:
                result.extend(self.quick_sort(s[i+2:]))
            return result


a1 = [6, 5, 3, 1, 8, 7, 2, 4]
# a1 = [6, 7, 10, 7, 8, 9]
# a1 = [21, 25, 49, 25, 16, 8]
# a1 = list(range(0, 10000))
# random.shuffle(a1)

s = Solution()
t1 = time.time()
# for i in range(100):
str = s.quick_sort(a1)
t2 = time.time()
print(t2-t1)
print(str)
