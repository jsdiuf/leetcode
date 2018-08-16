"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 15:57
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        1->(2)->3->(4)->5->(6)->7
        """
        if not head or not head.next:
            return head
        second = head.next
        p, q = head, head.next
        while 1:
            p.next = q.next
            if not p.next:
                break
            p = p.next
            q.next = p.next
            q = q.next
            if not q:
                break
        p.next = second
        return head


n = ListNode(1)
# n.next=ListNode(2)
# n.next.next=ListNode(3)
# n.next.next.next=ListNode(4)
# n.next.next.next.next=ListNode(5)
# n.next.next.next.next.next=ListNode(6)

s = Solution()
h = s.oddEvenList(n)
print(1)
