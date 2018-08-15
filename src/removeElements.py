"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 15:16
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next

        cur = head
        while cur:
            mv = cur.next
            while mv and mv.val == val:
                mv = mv.next
            cur.next = mv
            cur = mv
        return head

    def removeElements2(self, head, val):

        dummy = cur = ListNode(0)
        dummy.next = head
        while cur:
            mv = cur.next
            while mv and mv.val == val:
                mv = mv.next
            cur.next = mv
            cur = mv
        return dummy.next


n = ListNode(1)
n.next = ListNode(4)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(4)
n.next.next.next.next.next = ListNode(6)
s = Solution()
t = s.removeElements2(n, 4)
print(1)
