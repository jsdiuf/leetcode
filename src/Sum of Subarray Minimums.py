"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-16 10:35
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""


class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        L = len(A)
        A.sort()

        jc = [0]
        t = 1
        for i in range(1, L + 1):
            t *= i
            jc.append(t)

        def helper(n, m):
            return jc[n] / (jc[n - m] * jc[m])

        M = 2
        for i in range(1, L - 1):
            M += helper(L - 1, i)
        ans = 0
        for e in A:
            ans += e * M
        return ans % (10 ** 9 + 7)


s = Solution()
a=[0]*100
print(s.sumSubarrayMins(a))
