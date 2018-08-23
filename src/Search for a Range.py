"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-23 14:15

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def findtarget():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        def findleft(right):
            l, r = 0, right
            while l <= r:
                m = (l + r) // 2
                if m + 1 < len(nums) and nums[m + 1] == target and nums[m] < target:
                    return m + 1
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return 0

        def findright(left):
            l, r = left, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target and nums[m - 1] == target:
                    return m - 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return len(nums) - 1

        m = findtarget()
        return [-1, -1] if m == -1 else [findleft(m), findright(m)]

    def searchRange2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def findStart():
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    if mid - 1 < 0 or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        def findEnd():
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    if mid + 1 >= len(nums) or nums[mid + 1] > target:
                        return mid
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        return [findStart(), findEnd()]


s = Solution()
print(s.searchRange([1], 1))
