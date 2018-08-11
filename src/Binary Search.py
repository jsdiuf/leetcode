"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-10 23:48
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lth = len(nums)
        i, j = 0, lth - 1

        while i <= j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if mid == i or mid == j:
                return -1
            if nums[mid] > target:
                j = mid
            else:
                i = mid
        return -1


arr = [-1, 0, 3, 5, 9, 12]
target = -100
s = Solution()
print(s.search(arr, target))
