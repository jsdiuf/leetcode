"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 17:13
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        1->2->2->1
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True
