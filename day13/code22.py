# -*-coding:utf-8 -*-
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
top93.48%
"""
import time
import sys


class Solution(object):
    def add_candidate(self, candidate_list, i, k, count_l, count_r):
        # print(candidate_list)
        # print('i: {0}, l: {1}'.format(i, k))
        if i < k:
            # print('i = {0}'.format(i))
            i += 1
            if count_r + 1 <= count_l:
                new_candidate = [c + ')' for c in candidate_list]
                new_r = self.add_candidate(new_candidate, i, k, count_l, count_r + 1)
            else:
                # print('count_r + 1 > count_l')
                new_r = []
            if count_l - count_r < k - i:
                new_candidate = [c + '(' for c in candidate_list]
                new_l = self.add_candidate(new_candidate, i, k, count_l + 1, count_r)
            else:
                # print('count_l - count_r < k - 1 - i')
                new_l = []
            candidate_list = new_l + new_r
        else:
            return candidate_list
        return candidate_list

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parenthesis_candidate = ['(']

        count_l = 1
        count_r = 0

        parenthesis = self.add_candidate(parenthesis_candidate, 1, 2*n, count_l, count_r)

        return parenthesis

    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     parenthesis_candidate = ['(']
    #     parenthesis = []
    #
    #     for i in range(2*n-1):
    #         parenthesis_l = [p + '(' for p in parenthesis_candidate]
    #         parenthesis_r = [p + ')' for p in parenthesis_candidate]
    #         parenthesis_candidate = parenthesis_l + parenthesis_r
    #
    #     for candidate in parenthesis_candidate:
    #         count_left = 0
    #         count_right = 0
    #         for i in range(len(candidate)):
    #             if candidate[i] == '(':
    #                 count_left += 1
    #             else:
    #                 count_right += 1
    #             if count_left < count_right:
    #                 break
    #         if count_left == count_right:
    #             parenthesis.append(candidate)
    #
    #     return parenthesis

# a1 = "()"
# a1 = "()[]{}"
# a1 = "(]"
# a1 = "([)]"
a1 = 10
# a1 =

s = Solution()
t1 = time.time()
str = s.generateParenthesis(a1)
t2 = time.time()
print(t2-t1)
print(str)

# 1.1879990100860596