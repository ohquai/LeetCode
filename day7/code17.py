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

    def recursive(self, digit_num, c_list):
        if digit_num.__len__() > 1:
            c_list = self.recursive(digit_num[1:digit_num.__len__()], c_list)
            digit_alpha = self.dict_digit[int(digit_num[0])-2]
            return [e1+e2 for e1 in digit_alpha for e2 in c_list]
        else:
            return self.dict_digit[int(digit_num)-2]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits.__len__() == 0:
            return []

        combination_list = []
        c_list = self.recursive(digits, combination_list)
        return c_list


a = "23"
# a = "233"
# a = ''
# a = '6'
s = Solution()
t1 = time.time()
str = s.letterCombinations(a)
t2 = time.time()
print(t2-t1)
print(str)
