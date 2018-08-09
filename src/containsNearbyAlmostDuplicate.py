"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-9 9:49
"""
import time


class Solution:

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for idx, val in enumerate(nums):
            if val in d and idx - d[val] <= k:
                return True
            d[val] = idx
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int 距离
        :type t: int 最大差值
        :rtype: bool
        """
        d={}

        for idx,val in enumerate(nums):


            d[val]=idx

        return False

    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] / w]
        return False


s = Solution()
print(time.time())
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
# print(s.containsNearbyAlmostDuplicate2([], 10000, 0))
print(time.time())
