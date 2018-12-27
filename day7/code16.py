# -*-coding:utf-8 -*-
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
top 90%
"""
import time
import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_length = len(nums)
        if nums_length < 3:
            return sum([])
        nums.sort()
        threeSum = []

        # t1 = time.time()
        i_range = nums_length - 2

        min_ecart = sys.maxsize
        for i in range(i_range):
            # print(time.time() - t1)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = nums_length - 1
            while l < r:
                diff = nums[i] + nums[l] + nums[r] - target
                abs_diff = abs(diff)

                if abs_diff < min_ecart:
                    min_ecart = abs_diff
                    threeSum = [nums[i], nums[l], nums[r]]

                if diff == 0:
                    return sum(threeSum)
                elif diff > 0:
                    r -= 1
                    while nums[r + 1] == nums[r] and l < r:
                        r -= 1
                else:
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1

            if nums[i] > target:
                break
        return sum(threeSum)


# a = [0, 2, 1, -3]
a = [-1, 2, 1, -4]
target = 1

s = Solution()
t1 = time.time()
str = s.threeSumClosest(a, target)
t2 = time.time()
print(t2-t1)
print(str)
