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
        d = {}
        div = t
        if t == 0:
            div = 1
        if t < 0:
            return False
        for idx, val in enumerate(nums):
            key = val // div

            if key in d:
                return True
            if key - 1 in d and abs(nums[d[key - 1]] - val) <= t:
                return True
            if key + 1 in d and abs(nums[d[key + 1]] - val) <= t:
                return True
            d[key] = idx
            if idx >= k:
                del d[nums[idx - k] // div]
        return False


s = Solution()
print(s.containsNearbyAlmostDuplicate([-1, -1], 1, 1))
# print(s.containsNearbyAlmostDuplicate2([], 10000, 0))
