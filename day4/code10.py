# -*-coding:utf-8 -*-
"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
"""
import time


class Solution(object):
    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     m, n = len(s), len(p)
    #     dp = [[False] * (n+1) for _ in range(m+1)]
    #     dp[0][0] = True
    #     for i in range(0, m+1):
    #         for j in range(1, n+1):
    #             if p[j-1] == '*':
    #                 dp[i][j] = dp[i][j-2] or ( i>0 and (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
    #             else:
    #                 dp[i][j] = i>0 and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
    #     print(dp)
    #     return dp[m][n]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        match_matrix = [[False] * (n+1) for _ in range(m+1)]
        match_matrix[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    # 如果p对应的不是*，则只要match_matrix[i - 1][j - 1]是成立的，且s[i-1]和p[j-1]也是对应的，则match_matrix[i][j]必成立
                    match_matrix[i][j] = i > 0 and match_matrix[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    # 两种情况，第一种*代表0，则只要match_matrix[i][j-2]成立，无论p[j-2]是什么，match_matrix[i][j]必定成立
                    # 第二种*代表1或多个，match_matrix[i-1][j]必须成立，可以理解为（*等于1的match_matrix[i][j]成立时，*等于0的match_matrix[i-1][j]必定也要成立，
                    # 而*大于1的情况则很明确了），同时且s[i-1]和p[j-2]也是对应的（此时p[j-1] = *，对应了p[j-2]的值）
                    match_matrix[i][j] = match_matrix[i][j-2] or (i>0 and match_matrix[i-1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        return match_matrix[m][n]

"""    
         c      *      a      *     b
a     [[True, False, True,  False, True,  False],
a     [False, False, False, True,  True,  False],
b     [False, False, False, False, True,  False],
      [False, False, False, False, False, True]]

"""
# a=121
a = "aab"
p = "c*a*b"
a = "mississppi"
p = "mis*is*p*."
# a=2**29

s = Solution()
t1 = time.time()
str = s.isMatch(a, p)
t2 = time.time()
print(t2-t1)
print(str)

"""
[
[True, False, False, False, False, False, False, False, False, False, False]
[False, True, False, False, False, False, False, False, False, False, False]
[False, False, True, False, True, False, False, False, False, False, False]
[False, False, False, True, True, False, False, False, False, False, False]
[False, False, False, False, True, False, False, False, False, False, False]
[False, False, False, False, False, True, False, True, False, True, False]
[False, False, False, False, False, False, True, True, False, True, True]
[False, False, False, False, False, False, False, True, False, True, True]
[False, False, False, False, False, False, False, False, True, True, True]
[False, False, False, False, False, False, False, False, False, True, True]
[False, False, False, False, False, False, False, False, False, False, True]
]


"""