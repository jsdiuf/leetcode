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

        if k == 1 or head is None:
            return head

        right = head
        step = 0
        # 查看尾部是否还有k个节点
        while right and step < k:
            right = right.next
            step += 1
        if step < k:
            return head

        # reserve
        p = t = head
        pl = None
        pr = p.next

        while pr is not right:
            p.next = pl
            pl = p
            p = pr
            pr = pr.next
        p.next = pl

        t.next = self.reverseKGroup(right, k)
        return p


s = Solution()

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n1.next.next.next = ListNode(4)
n1.next.next.next.next = ListNode(5)
#n1.next.next.next.next.next = ListNode(6)

h = s.reverseKGroup(n1, 5)
print(1)
