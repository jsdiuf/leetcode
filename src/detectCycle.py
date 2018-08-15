"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 20:47
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        fast = slow = head
        s = set()
        s.add(slow)

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow in s:
                return slow
            s.add(slow)
            if fast == slow:
                while 1:
                    if slow.next in s:
                        return slow.next
                    slow = slow.next

        return None


n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(0)
n4=ListNode(-4)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2
s=Solution()
print(s.detectCycle(n1).val)
