"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-22 15:08
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        0,1,2,3,4,5,6,7,8,9
        3,4,5,6,7,8,9,|0,1,2
        8,9,|0,1,2,3,4,5,6,7
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1

        while 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if left > right:
                return -1
            # 左边递增的  右边增减
            if nums[mid] > nums[left]:
                if target < nums[mid] and target > nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


s = Solution()
print(s.search([8, 9, 0, 1, 2, 3, 4, 5, 6, 7], 0))
