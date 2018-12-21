# -*-coding:utf-8 -*-
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
import time


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

# a=121
a=-123
# a=123
# a=2**29

s = Solution()
t1 = time.time()
str = s.isPalindrome(a)
t2 = time.time()
print(t2-t1)
print(str)
