"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-13 21:10
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [-2,1,-3,4,-1,2,1,-5,4],
        """
        if not nums:
            return None
        maxnum = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = (nums[i] + dp[i - 1]) if dp[i - 1] > 0 else nums[i]
            maxnum = max(dp[i], maxnum)
        return maxnum

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [-2,1,-3,4,-1,2,1,-5,4],
        """
        if not nums:
            return None
        maxnum = nums[0]
        maxendwithi = nums[0]

        for i in range(1, len(nums)):
            maxendwithi = max(maxendwithi + nums[i], nums[i])
            maxnum = max(maxendwithi, maxnum)
        return maxnum


s = Solution()
print(s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
