"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-29 9:26
@desc:

Given an integer array, return the k-th smallest distance among all the pairs.
The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""
import time


class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        [1,3,5,7,7,8,8,12]
        [1,2,3,4,5]
        """
        nums.sort()
        n = len(nums)

        def helper(mid):
            cnt = 0
            for i in range(n - 1):
                j = i
                while j < n and nums[j] <= nums[i] + mid:
                    j += 1
                cnt += j - i + 1
            return cnt

        l, r = 0, nums[-1] - nums[0]

        while l <= r:
            m = (l + r) // 2

            cnt = helper(m)
            if cnt < k:
                l = m + 1
            else:
                r = m - 1
        return l

    def smallestDistancePair2(self, nums, k):

        nums.sort()

        n = len(nums)
        l, r = 0, nums[n - 1] - nums[0]

        while l < r:
            cnt = 0
            m = (r + l) // 2

            j = 0
            for i in range(n):
                while j < n and nums[j] <= nums[i] + m:
                    j += 1
                cnt += j - i - 1

            if cnt < k:
                l = m + 1
            else:
                r = m
        return l


s = Solution()
print(s.smallestDistancePair2(
    [1, 2, 3, 4, 5, 7, 7, 7, 9],
    5))
