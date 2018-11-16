"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-16 17:29
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    #48ms
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

        #40ms
        def hasCycle2(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            if head is None or head.next is None:
                return False
            slow = head
            fast = head.next
            while fast and fast.next:
                if slow == fast:
                    return True

                slow = slow.next
                fast = fast.next.next

            return False


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n7

s = Solution()
print(s.hasCycle(n1))
