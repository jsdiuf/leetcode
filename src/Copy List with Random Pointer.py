"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-27 14:38
A linked list is given such that each node contains
an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = {}
        if not head:
            return
        p1 = head
        dummy = p2 = RandomListNode(0)
        while p1:
            p2.next = RandomListNode(p1.label)
            p2 = p2.next
            dic[p1] = p2
            p2.random = p1.random
            p1 = p1.next
        cur = dummy.next
        while cur:
            if cur.random:
                cur.random = dic[cur.random]
            cur = cur.next
        return dummy.next


s = Solution()

n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n4 = RandomListNode(4)
n5 = RandomListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n1.random = n4

r = s.copyRandomList(n1)
print(1)
