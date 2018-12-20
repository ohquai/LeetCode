# -*-coding:utf-8 -*-
import time


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = s
        s2 = s[::-1]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    pass



a="pwwkekw"
# a="abcabcbb"
# a="bbbbb"
# a="dvdf"
s = Solution()
t1 = time.time()
len = s.longestPalindrome(a)
t2 = time.time()
print(t2-t1)
print(len)
