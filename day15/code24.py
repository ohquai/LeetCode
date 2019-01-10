# -*-coding:utf-8 -*-
"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
给定 1->2->3->4, 你应该返回 2->1->4->3.
top45%
"""
import time
import sys


def print_listNode(l):
    r = [l.val]
    while l.next is not None:
        l = l.next
        r.append(l.val)
    print(r)
    # return r


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swap_two(self, listnode):
        if listnode.next is not None:
            A = ListNode(listnode.next.val)
            B = ListNode(listnode.val)
            A.next = B
            B.next = listnode.next.next
            return A
        else:
            return listnode

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            swap_head = self.swap_two(head)
            # print_listNode(swap_head)
            last_head = swap_head.next
            while last_head is not None and last_head.next is not None:
                top_two = self.swap_two(last_head.next)
                last_head.next = top_two
                last_head = top_two.next
                # print_listNode(swap_head)

        return swap_head


a1 = ListNode(1)
# a2 = ListNode(2)
# a3 = ListNode(3)
# a4 = ListNode(4)
# a5 = ListNode(5)
# a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

s = Solution()
t1 = time.time()
str = s.swapPairs(a1)
t2 = time.time()
print(t2 - t1)
print_listNode(str)
# print(str.next)
