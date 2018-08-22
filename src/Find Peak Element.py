"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-22 16:39
"""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return None
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l, r = 1, len(nums) - 2

        while l <= r:
            if nums[l] > nums[l + 1]:
                return l
            if nums[r] > nums[r - 1]:
                return r
            l += 1
            r -= 1


s = Solution()
print(s.findPeakElement([1, 2, 3, 2]))
