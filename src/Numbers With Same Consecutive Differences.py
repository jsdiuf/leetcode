"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018/12/30 10:59
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
Note:

1 <= N <= 9
0 <= K <= 9
"""


class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """

        if N == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        ans = []

        def backtrace(len, num):
            if len == N:
                ans.append(num)
                return
            n = num % 10
            if 0 <= n - K <= 9:
                backtrace(len + 1, num * 10 + n - K)
            if 0 < n + K <= 9 and K != 0:
                backtrace(len + 1, num * 10 + n + K)

        for i in range(1, 10):
            backtrace(1, i)

        return ans


s = Solution()
print(s.numsSameConsecDiff(2, 0))
