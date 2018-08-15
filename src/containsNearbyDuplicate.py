"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 10:50
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        1,2,3,1,2,3  k=2
        """
        dic = {}
        for idx, val in enumerate(nums):
            if val in dic and idx - dic[val] <= k:
                return True
            dic[val] = idx
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
