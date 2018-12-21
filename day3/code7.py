# -*-coding:utf-8 -*-
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""
import time


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            r = int(str(abs(x))[::-1]) * (-1)
            if r < -2147483648:
                return 0
            else:
                return r
        else:
            r = int(str(abs(x))[::-1])
            if r > 2147483647:
                return 0
            else:
                return r

a=120
a=-123
a=123
a=2**29

s = Solution()
t1 = time.time()
str = s.reverse(a)
t2 = time.time()
print(t2-t1)
print(str)
