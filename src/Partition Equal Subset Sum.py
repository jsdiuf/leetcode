"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-11 16:22
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        sum = 0
        for e in nums:
            sum += e
        if sum & 1 == 1:
            return False

        dp = [False for i in range(sum + 1)]
        dp[0] = True
        sum //= 2
        for e in nums:
            for i in range(sum, 0, -1):
                if i >= e:
                    dp[i] = dp[i] or dp[i - e]
        return dp[sum]

    def canPartition2(self,nums):
        if not nums:
            return True
        W = sum(nums)
        if W & 1 == 1:
            return False
        W //= 2
        #         dp=[False]*(W+1)

        #         for i in range(1,len(nums)):
        #             for j in range(W,nums[i]-1,-1):
        #                 dp[j]|=nums[i]==j or dp[j-nums[i]]

        #         return dp[W]

        nums.sort(reverse=True)

        def dfs(nums, sum1, sum2):
            nonlocal W
            if sum1 > W or sum2 > W:
                return False
            elif not nums:
                return sum1 == sum2
            else:
                return dfs(nums[1:], sum1 + nums[0], sum2) or dfs(nums[1:], sum1, sum2 + nums[0])

        return dfs(nums, 0, 0)


s = Solution()
print(s.canPartition2([1, 5, 11, 6]))