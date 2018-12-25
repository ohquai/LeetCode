# -*-coding:utf-8 -*-
"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
"""
import time


class Solution(object):
    def best_side(self, subHeight):
        """
        两边相同时，往内搜索，如果单边随机选有可能选不到最好的
        :param subHeight:
        :return:
        """
        best_side = 'index_left'
        index_left = 0
        index_right = len(subHeight) - 1
        for i in range(1, int(len(subHeight)/2-1)):
            index_left += 1
            index_right -= 1
            if subHeight[index_left]<subHeight[index_right]:
                best_side = 'index_left'
            elif subHeight[index_left]>subHeight[index_right]:
                best_side = 'index_right'
        return best_side

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 1 or height == []:
            return 0
        max_area = 0
        index_left = 0
        index_right = len(height)-1
        while index_right-index_left >= 1:
            min_height = min(height[index_left], height[index_right])
            area = min_height * (index_right-index_left)
            if area > max_area:
                max_area = area
            if height[index_left]<height[index_right]:
                index_left += 1
            elif height[index_left]>height[index_right]:
                index_right -= 1
            elif index_right-index_left <= 3:
                index_left += 1
            else:
                best_side = self.best_side(height[index_left:index_right+1])
                if best_side == 'index_left':
                    index_left += 1
                else:
                    index_right -= 1
        return max_area





# a=121
a = [1,8,6,2,5,4,8,3,7]
# a=2**29

s = Solution()
t1 = time.time()
str = s.maxArea(a)
t2 = time.time()
print(t2-t1)
print(str)
