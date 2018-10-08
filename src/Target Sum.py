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


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        ans = 0
        q = [[], [-nums[0], nums[0]]]
        for i in range(1, len(nums)):
            t = []
            for e in q[1]:
                t.append(e + nums[i])
                t.append(e - nums[i])
            q[0] = q[1]
            q[1] = t
        for e in q[-1]:
            if e == S:
                ans += 1
        return ans


s = Solution()
print(s.findTargetSumWays([29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38], 35))
