"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 22:11
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        l_a = l_b = 0
        mva, mvb = headA, headB
        while mva:
            l_a += 1
            mva = mva.next
        while mvb:
            l_b += 1
            mvb = mvb.next
        mva, mvb = headA, headB
        if l_a > l_b:
            step = l_a - l_b
            while step:
                mva = mva.next
                step -= 1
        if l_b > l_a:
            step = l_b - l_a
            while step:
                mvb = mvb.next
                step -= 1
        while mva != mvb:
            if not mva or not mvb:
                return None
            mva = mva.next
            mvb = mvb.next
        return mva


