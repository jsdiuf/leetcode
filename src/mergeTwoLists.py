"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-17 9:41
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
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        """
        dummy = cur = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next


n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(4)
n1.next.next.next = ListNode(5)
n1.next.next.next.next = ListNode(6)

n2 = ListNode(1)
n2.next = ListNode(3)
n2.next.next = ListNode(4)

s = Solution()
h = s.mergeTwoLists(n1, n2)
print(1)
