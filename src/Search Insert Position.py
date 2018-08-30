"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-29 23:04
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        l, r, n = 0, len(nums) - 1, len(nums)

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if m < n - 1 and nums[m] < target and nums[m + 1] > target:
                return m + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1

    def searchInsert2(self, nums, target):
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l


s = Solution()
print(s.searchInsert2([1, 2, 3, 4, 6, 7], 5))
