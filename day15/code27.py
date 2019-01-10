# -*-coding:utf-8 -*-
"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
top98%
"""
import time
import sys


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        val_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[val_index] = nums[i]
                val_index += 1
            # print(nums)
        return val_index

nums = [0,1,2,2,3,0,4,2]
val = 5
# a1 = [1, 1, 2]
a1 = []

s = Solution()
t1 = time.time()
index_dedup = s.removeElement(nums, val)
t2 = time.time()
print(t2-t1)
print(nums[:index_dedup])
