# -*-coding:utf-8 -*-
"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
99%
"""
import time
import sys


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


haystack = "hello"
needle = "ll"
haystack = "aaaaa"
needle = ""

s = Solution()
t1 = time.time()
result = s.strStr(haystack, needle)
t2 = time.time()
print(t2-t1)
print(result)
