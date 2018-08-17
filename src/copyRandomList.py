"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-17 16:01
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

        dummy = cur = RandomListNode(0)
        mv = head
        map = {}
        while mv:
            cur.next = RandomListNode(mv.label)
            cur = cur.next
            # 找到映射关系
            map[mv] = cur
            if mv.random:
                cur.random = mv.random
            mv = mv.next

        cur = dummy.next
        while cur:
            if cur.random:
                cur.random = map[cur.random]
            cur = cur.next
        return dummy.next
