"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-9 0:59
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
 which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
import time
from math import sqrt


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        end = int(sqrt(n))
        if end * end == n:
            return 1
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(n + 1):
            j = 1
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


s = Solution()
print(time.time())
print(s.numSquares(3081))
print(time.time())
