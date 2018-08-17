"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-17 17:15
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        n = 0
        cur = head
        # get the lenght
        tail=None
        while cur:
            n += 1
            if not cur.next:
                tail=cur
            cur = cur.next
        right = k % n
        if right == 0:
            return head
        cur = head
        step = n - right
        # get the new linkList head
        while step > 1:
            cur = cur.next
            step -= 1
        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(5)

s = Solution()
h = s.rotateRight(n, 2)
print(1)
