"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-4 18:05
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode("")
        pre.next = head
        self.recur(pre, head)
        return pre.next

    def recur(self, pre, curr):
        if curr and curr.next:
            pre.next = curr.next
            curr.next = curr.next.next
            pre.next.next = curr
            self.recur(curr, curr.next)

    # wonderful
    def swapPairs2(self, head):
        if head is None or head.next is None:
            return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n


n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
# n1.next.next.next = ListNode(4)
s = Solution()
head = s.swapPairs(n1)
print(1)
