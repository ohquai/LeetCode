# -*-coding:utf-8 -*-
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""
import time
import sys


class Solution(object):
    def __init__(self):
        self.dict_digit = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
                           ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits.__len__() == 0:
            return []

        alphabet_s = [self.dict_digit[int(i)-2] for i in digits]
        stack = [alpha for alpha in alphabet_s[0]]  # 此处没安装copy

        for i in range(1, len(alphabet_s)):
            iter = len(stack)
            for _ in range(iter):
                temp = stack.pop(0)
                [stack.append(temp + ch) for ch in alphabet_s[i]]

        return stack


a = "23"
# a = "233"
a = '22'
# a = ''
# a = '6'
s = Solution()
t1 = time.time()
str = s.letterCombinations(a)
t2 = time.time()
print(t2-t1)
print(str)
