"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-29 17:52
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
import time

from scipy._lib.six import xrange


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums: return 0

        total = sum(nums)
        if not -total <= S <= total or (total - S) % 2 == 1: return 0

        # Note all the possible sums we can get are symmetric,
        # i.e. if there are n ways to get a sum S, there must
        # also be n ways to get -S.
        target = (total - S) // 2
        dp = [0] * (target + 1)
        dp[0] = 1  # when S == total

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[target]


s = Solution()
print(time.time())
print(s.findTargetSumWays([1], 1))
print(time.time())
