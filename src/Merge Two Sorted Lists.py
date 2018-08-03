"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-3 12:00
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
                move = move.next
        move.next = l1 or l2
        return head.next

    # 递归版
    def mergeTwoListsRecursion(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursion(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursion(l1, l2.next)
            return l2


s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)

n1.next = n2
n2.next = n3

m1 = ListNode(1)
m2 = ListNode(3)
m3 = ListNode(4)

m1.next = m2
m2.next = m3

head = s.mergeTwoLists(n1, m1)
print(1)
