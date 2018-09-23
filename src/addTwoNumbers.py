"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-17 9:56
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jw = 0
        dummy = cur = ListNode(0)

        while l1 and l2:
            sum = l1.val + l2.val + jw
            cur.next = ListNode(sum % 10)
            cur = cur.next
            jw = sum // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + jw
            cur.next = ListNode(sum % 10)
            cur = cur.next
            jw = sum // 10
            l1 = l1.next
        while l2:
            sum = l2.val + jw
            cur.next = ListNode(sum % 10)
            cur = cur.next
            jw = sum // 10
            l2 = l2.next
        if jw != 0:
            cur.next = ListNode(1)
        return dummy.next

    def addTwoNumbers2(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next


l1 = ListNode(5)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
h = s.addTwoNumbers2(l1, l2)
print(1)
