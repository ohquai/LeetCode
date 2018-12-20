# -*-coding:utf-8 -*-
import time


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        carry_val = 0
        first_node = ListNode(0)
        result_node = first_node
        node1 = l1
        node2 = l2
        # 输入：(4 -> 4 -> 3) + (5 -> 6 -> 4)
        # 输出：9 -> 0 -> 8
        while node1.val is not None or node2.val is not None:
            new_val = node1.val + node2.val + carry_val
            # print('{0}+{1}+{2} = {3}'.format(node1.val, node2.val, carry_val, new_val))
            if new_val >= 10:
                new_val -= 10
                carry_val = 1
            else:
                carry_val = 0
            new_node = ListNode(new_val)
            result_node.next = new_node
            result_node = result_node.next

            if node1.next is None and node2.next is None:
                break
            elif node1.next is None:
                node1 = ListNode(0)
                node2 = node2.next
            elif node2.next is None:
                node1 = node1.next
                node2 = ListNode(0)
            else:
                node1 = node1.next
                node2 = node2.next
                # print(node1.val)
                # print(node2.val)

        if carry_val == 1:
            new_node = ListNode(1)
            result_node.next = new_node
        return first_node.next

# [2,4,3]
# [5,6,4]
a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

s = Solution()
r = s.addTwoNumbers(a1, b1)

while r.next is not None:
    print(r.val)
    r = r.next
print(r.val)
