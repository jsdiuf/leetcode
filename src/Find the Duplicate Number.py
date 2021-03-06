"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-25 15:56
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for e in nums:
            if e in s: return e
            s.add(e)

    # 下一个元素的下标 是这个元素的值
    def findDuplicate2(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow


s = Solution()
print(s.findDuplicate2([4, 3, 1, 4, 2]))
# 2,5,6,8,9,1,4,5,0
