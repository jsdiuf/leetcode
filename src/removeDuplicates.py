"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 15:48
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max = nums[0]
        index = 1

        for i in range(len(nums)):
            while nums[i] > max:
                max = nums[i]
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        return index


s = Solution()
s.removeDuplicates([0, 0])
