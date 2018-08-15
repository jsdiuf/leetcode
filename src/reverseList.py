"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 14:13
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # recursion
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        r = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return r

    # iterator
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


n = ListNode(1)
# n.next = ListNode(2)
# n.next.next = ListNode(3)
# n.next.next.next=ListNode(4)
s = Solution()
tt = s.reverseList2(None)
print(1)
