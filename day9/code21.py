# -*-coding:utf-8 -*-
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
import time
import sys


def print_listNode(l):
    r = [l.val]
    while l.next is not None:
        l = l.next
        r.append(l.val)
    return r


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
        current_node = new_node = ListNode(0)
        while l1 is not None and l2 is not None:
            # print(print_listNode(l1))
            # print(print_listNode(l2))
            if l1.val <= l2.val:
                current_node.next = l1
                current_node = current_node.next
                l1 = l1.next
            else:
                current_node.next = l2
                current_node = current_node.next
                l2 = l2.next

        while l1 is not None:
            current_node.next = l1
            current_node = current_node.next
            l1 = l1.next
        while l2 is not None:
            current_node.next = l2
            current_node = current_node.next
            l2 = l2.next

        return new_node.next



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

# a1 = ListNode(2)
#
# b1 = ListNode(1)

# a1 = ListNode(5)
#
#
# b1 = ListNode(1)
# b2 = ListNode(2)
# b3 = ListNode(4)
# b1.next = b2
# b2.next = b3

s = Solution()
t1 = time.time()
str = s.mergeTwoLists(a1, b1)
t2 = time.time()
print(t2 - t1)
print(print_listNode(str))
# print(str.next)
