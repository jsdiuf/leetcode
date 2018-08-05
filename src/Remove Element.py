"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 18:09
"""


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        right = len(nums) - 1
        left = 0
        while left < right:

            while left < right and nums[right] == val:
                right -= 1
                continue
            while left < right and nums[left] != val:
                left += 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
        if nums[0] == val:
            return 0
        return left + 1


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
