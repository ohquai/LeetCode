# -*-coding:utf-8 -*-
"""
编写一个函数来查找字符串数组中的最长公共前缀。
top 50%
"""
import time


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_length = len(strs)
        if strs_length == 0:
            return ""

        min_len = min([len(s) for s in strs])
        if min_len == 0:
            return ""

        for i in range(strs_length-1):
            comme_len = 0
            for j in range(min_len):
                if strs[i][j] == strs[i+1][j]:
                    comme_len += 1
                else:
                    break
            if comme_len < min_len:
                min_len = comme_len
            if comme_len == 0:
                return ""
        return strs[0][0:min_len]



# a=121
a = ["flower","flow","flight"]
# a = ["dog","racecar","car"]
a = [""]

s = Solution()
t1 = time.time()
str = s.longestCommonPrefix(a)
t2 = time.time()
# print(t2-t1)
print(str)
