# -*-coding:utf-8 -*-
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
"""
import time
import sys
import copy

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
    def quick_sort(self, s):
        """
        :type s: list
        :rtype: list
        """
        if len(s) == 1:
            return s
        else:
            h = s[-1]
            i = -1
            for j in range(len(s)-1):
                if s[j] <= h:
                    i += 1
                    tmp = s[i]
                    s[i] = s[j]
                    s[j] = tmp
                # print('i: {0}, j:{1}'.format(i, j))
                # print(s)
            tmp = s[i+1]
            s[i+1] = s[-1]
            s[-1] = tmp
            # print('{0} epoch finish'.format(j))
            # print(s)

            result = []
            if i + 1 > 0:
                result.extend(self.quick_sort(s[:i+1]))
            result.append(s[i+1])
            if i + 1 < len(s)-1:
                result.extend(self.quick_sort(s[i+2:]))
            return result

    def mergeKLists(self, lists):
        """
        合并到list，进行快排
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        qs_list = []
        for i in range(len(lists)):
            listnode = lists[i]
            while listnode is not None and listnode.val is not None:
                qs_list.append(listnode.val)
                listnode = listnode.next

        if qs_list == []:
            return None

        qs_list = self.quick_sort(qs_list)
        # print(qs_list)

        r_listnode = current_listnode = ListNode(0)
        for qs in qs_list:
            current_listnode.next = ListNode(qs)
            current_listnode = current_listnode.next
        return r_listnode.next

    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     current_node = new_node = ListNode(0)
    #     while l1 is not None and l2 is not None:
    #         # print(print_listNode(l1))
    #         # print(print_listNode(l2))
    #         if l1.val <= l2.val:
    #             current_node.next = l1
    #             current_node = current_node.next
    #             l1 = l1.next
    #         else:
    #             current_node.next = l2
    #             current_node = current_node.next
    #             l2 = l2.next
    #
    #     while l1 is not None:
    #         current_node.next = l1
    #         current_node = current_node.next
    #         l1 = l1.next
    #     while l2 is not None:
    #         current_node.next = l2
    #         current_node = current_node.next
    #         l2 = l2.next
    #
    #     return new_node.next

    # def mergeKLists(self, lists):
    #     """
    #     通过两两归并合并，进行连接
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     if len(lists) == 0:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #
    #     new_node = self.mergeTwoLists(lists[0], lists[1])
    #     if len(lists) == 2:
    #         return new_node
    #     else:
    #         for i in range(2, len(lists)):
    #             new_node = self.mergeTwoLists(new_node, lists[i])
    #         return new_node



a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(5)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

c1 = ListNode(2)
c2 = ListNode(6)
c1.next = c2

l = [a1, b1, c1]

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
str = s.mergeKLists(l)
t2 = time.time()
print(t2 - t1)
print_listNode(str)
# print(str.next)
