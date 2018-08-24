"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-24 14:55
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1,2]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

it's a litter diffcult
"""


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [3,4,5,5,5,6,6,1,1,2,3,3]
        [3,3,3,1]
        [1]
        [1,1]
        [2,2,2,0,1,2]
        [10,1,10,10,10]
        """

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r] or len(nums) == 1:
            return nums[l]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        while l < r:
            m = (l + r) // 2
            if m + 1 < len(nums) and nums[m] > nums[m + 1]:
                return nums[m + 1]
            if m - 1 >= 0 and nums[m - 1] > nums[m]:
                return nums[m]
            if nums[l] == nums[m] == nums[r]:
                return min(self.findMin(nums[l:m + 1]), self.findMin(nums[m:r + 1]))
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]

    # clever
    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        # ans = nums[left]

        while left < right:
            mid = (right - left) // 2 + left
            if nums[right] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


s = Solution()
print(s.findMin([2, 2, 2, 0, 1, 2]))
