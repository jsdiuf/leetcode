"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-6 15:49
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        i, j = 0, len(nums) - 1

        while i < j:
            while i < j and nums[i] != 0:
                i += 1
            if not i < j:
                break
            nums.append(nums[i])
            del nums[i]
            j -= 1
        print(nums)

        """
        idx = 0 
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        """


s = Solution()
print(s.moveZeroes([1]))
