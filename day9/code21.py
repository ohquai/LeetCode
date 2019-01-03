# -*-coding:utf-8 -*-
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
import time
import sys


class ListNode(object):
    def __init__(self, x):
            self.val = x
            self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

s = Solution()
t1 = time.time()
str = s.mergeTwoLists(a1, b1)
t2 = time.time()
print(t2-t1)
print(str)
print(str.next)
