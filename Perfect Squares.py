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


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        def helper(N):
            l, r = 1, N
            while l <= r:
                m = (l + r) // 2
                if m ** 2 <= N and (m + 1) ** 2 > N:
                    return N - m ** 2
                if m ** 2 < N:
                    l = m + 1
                else:
                    r = m - 1

        count = 0
        while n:
            count += 1
            n = helper(n)
        return count


s = Solution()
print(s.numSquares(13))
