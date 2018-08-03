"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-2 22:43
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        pre = ListNode("")
        pre.next = head
        p1 = pre
        p2 = pre
        while p1 and n >= 0:
            p1 = p1.next
            n -= 1
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return pre.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
# n3.next = n4
# n4.next = n5

s = Solution()
head = s.removeNthFromEnd(n1, 2)
print(n1)
