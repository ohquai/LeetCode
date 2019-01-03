# -*-coding:utf-8 -*-
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
top93%
"""
import time
import sys


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True

        if s.__len__() % 2 != 0:
            return False

        stack = ""
        for i in range(s.__len__()):
            if s[i] == "{":
                stack += "}"
            elif s[i] == "[":
                stack += "]"
            elif s[i] == "(":
                stack += ")"
            else:
                if stack == "":
                    return False
                elif s[i] != stack[-1]:
                    return False
                else:
                    stack = stack[:-1]
        if stack != "":
            return False
        else:
            return True


a1 = "()"
# a1 = "()[]{}"
# a1 = "(]"
# a1 = "([)]"
a1 = "{[]}"
# a1 =

s = Solution()
t1 = time.time()
str = s.isValid(a1)
t2 = time.time()
print(t2-t1)
print(str)
