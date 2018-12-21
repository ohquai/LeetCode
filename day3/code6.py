# -*-coding:utf-8 -*-
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
"""
import time


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        if numRows >= s.__len__():
            return s

        new_s = ""
        i = 0
        # 构建首行
        while i <= s.__len__() - 1:
            # print(i)
            new_s += s[i]
            # print(new_s)
            i += (2 * numRows - 2)

        # 构建中间
        for k in range(1, numRows-1):
            i = k
            last_left = 0
            while i + (numRows - 1 - k) + (numRows - 2 -k) + 1 <= s.__len__()-1:
                # print(i)
                new_s += s[i]
                # print(new_s)
                new_s += s[i + (numRows - 1 - k) + (numRows - 2 -k) + 1]
                # print(new_s)
                i += (2*numRows -2)
                last_left = i

            if last_left <= s.__len__()-1:
                new_s += s[i]
                # print(new_s)

        # 填充尾行
        i = numRows - 1
        while i <= s.__len__() - 1:
            # print(i)
            new_s += s[i]
            # print(new_s)
            i += (2 * numRows - 2)

        return new_s


a="LEETCODEISHIRING"
a='LEETCODEISHIRING'
# a="babad"
# a="cbbd"

s = Solution()
t1 = time.time()
str = s.convert(a, 3)
t2 = time.time()
print(t2-t1)
print(str)
