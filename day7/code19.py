# -*-coding:utf-8 -*-
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""
import time
import sys


class ListNode(object):
    def __init__(self, x):
            self.val = x
            self.next = None


class Solution(object):
    def remove_n(self, head, n, i):
        if head.next is not None:
            _, i = self.remove_n(head.next, n, i)
            i += 1
            if i == n+1:
                head.next = head.next.next
            return head, i
        else:
            return head, i

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return

        head, node_len = self.remove_n(head, n, 1)
        if node_len == n:
            return head.next
        print(node_len)
        return head


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
n = 2

a1 = ListNode(1)
n = 1

a1 = ListNode(1)
a2 = ListNode(2)
a1.next = a2
n = 2

s = Solution()
t1 = time.time()
str = s.removeNthFromEnd(a1, n)
t2 = time.time()
print(t2-t1)
print(str)
print(str.next)
