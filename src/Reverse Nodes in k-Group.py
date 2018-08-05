"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-4 21:01
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = ListNode("")
        pre.next = head
        self.recur(pre, head, k)
        return pre.next

    def recur(self, pre, curr, k):

        if curr and curr.next:
            right=curr
            dk=k-1
            while dk>0:
                right=right.next
                if right is None:
                    return
                dk-=1
            while dk<=k:
                self.reserveTwo()
