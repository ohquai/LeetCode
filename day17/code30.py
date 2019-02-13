# -*-coding:utf-8 -*-
"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

"""
import time
import sys


class Solution(object):
    def get_substring(self, s, words, word_len, index):
        if len(words) == 0 and index > 0:
            return True
        for i in range(len(words)):
            if s[index:index+word_len] == words[i]:
                index += word_len
                words = words[: i] + words[i+1:]
                r_bool = self.get_substring(s, words, word_len, index)
                if r_bool:
                    return r_bool
                else:
                    return False

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        word_len = len(words[0])

        index_list = []
        end = len(s) - word_len*len(words) + 1
        for i in range(0, end, 1):
            index = i
            if s[index:index + word_len] == words[i]:
                r_bool = True
                while len(words) != 0:
                    for i in range(len(words)):
                        if s[index:index + word_len] == words[i]:
                            index += word_len
                            words = words[: i] + words[i + 1:]
                            break
                    r_bool = False
                if r_bool:
                    index_list.append(index)
        return index_list

    # def get_substring(self, s, words, word_len, index):
    #     if len(words) == 0 and index > 0:
    #         return True
    #     for i in range(len(words)):
    #         if s[index:index + word_len] == words[i]:
    #             index += word_len
    #             words = words[: i] + words[i + 1:]
    #             r_bool = self.get_substring(s, words, word_len, index)
    #             if r_bool:
    #                 return r_bool
    #             else:
    #                 return False
    #
    # def findSubstring(self, s, words):
    #     """
    #     :type s: str
    #     :type words: List[str]
    #     :rtype: List[int]
    #     """
    #     if len(words) == 0:
    #         return []
    #     word_len = len(words[0])
    #
    #     index_list = []
    #     end = len(s) - word_len*len(words) + 1
    #     for i in range(0, end, 1):
    #         index = i
    #         r_bool = self.get_substring(s, words, word_len, index)
    #         if r_bool:
    #             index_list.append(index)
    #     return index_list


string = "barfoothefoobarman"
words = ["foo", "bar"]
string = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
words = ["good", "good", "best", "word"]

s = Solution()
t1 = time.time()
result = s.findSubstring(string, words)
t2 = time.time()
print(t2-t1)
print(result)
