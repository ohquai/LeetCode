# -*-coding:utf-8 -*-
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""
import time


# class Solution(object):
#     def return_max_Palindrome(self, str, x, y):
#         start = x
#         end = x
#         len = 1
#         while x>=0 and y<=str.__len__()-1 and str[x] == str[y]:
#             start = x
#             end = y
#             len = y - x + 1
#             x -= 1
#             y += 1
#         print('start:{0}, end:{1}, len:{2}'.format(start, end, len))
#         return start, end, len
#
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if s is None or s == '':
#             return 0
#
#         max_Palindrome_length = 1
#         Palindrome_start = 0
#         Palindrome_end = 0
#         for i in range(s.__len__()):
#             start1, end1, len1 = self.return_max_Palindrome(s, i, i)
#             start2, end2, len2 = self.return_max_Palindrome(s, i, i+1)
#             if len1 > len2:
#                 start = start1
#                 end = end1
#             else:
#                 start = start2
#                 end = end2
#             # print(i)
#             # print(s[start:end+1])
#             if end - start + 1 > max_Palindrome_length:
#                 max_Palindrome_length = end - start + 1
#                 Palindrome_start = start
#                 Palindrome_end = end
#         return max_Palindrome_length, s[Palindrome_start:Palindrome_end+1]


class Solution(object):
    def return_max_Palindrome(self, s, x, y):
        start = x
        end = x
        p_len = 1
        while x>=0 and y<=s.__len__()-1 and s[x] == s[y]:
            start = x
            end = y
            p_len = y - x + 1
            x -= 1
            y += 1
        return start, end, p_len

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or s == '':
            return ""

        max_Palindrome_length = 1
        Palindrome_start = 0
        Palindrome_end = 0
        s_len = s.__len__()
        for i in range(s_len):
            if i<s_len-1 and s[i] == s[i+1]:
                start1, end1, len1 = self.return_max_Palindrome(s, i, i)
                start2, end2, len2 = self.return_max_Palindrome(s, i, i+1)
                if len1 > len2:
                    start = start1
                    end = end1
                else:
                    start = start2
                    end = end2
            else:
                start, end, len = self.return_max_Palindrome(s, i, i)
            # print(i)
            # print(s[start:end+1])
            if end - start + 1 > max_Palindrome_length:
                max_Palindrome_length = end - start + 1
                Palindrome_start = start
                Palindrome_end = end
        return s[Palindrome_start:Palindrome_end+1]


a="pwwkekw"
# a="babad"
# a="cbbd"

s = Solution()
t1 = time.time()
str = s.longestPalindrome(a)
t2 = time.time()
print(t2-t1)
print(str)
