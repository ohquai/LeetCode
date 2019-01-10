# -*-coding:utf-8 -*-
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
top95%
"""
import time
import sys


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        index_dedup = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index_dedup]:
                nums[index_dedup + 1] = nums[i]
                index_dedup += 1
        return index_dedup+1


a1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# a1 = [1, 1, 2]
a1 = []

s = Solution()
t1 = time.time()
index_dedup = s.removeDuplicates(a1)
t2 = time.time()
print(t2-t1)
print(a1[:index_dedup])
