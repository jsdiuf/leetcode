"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-23 9:44
"""


class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        if len(A) == 1:
            return 0
        if len(A) == 2:
            return min(A[1] - A[0], abs(A[0] + K - A[1] + K))
        ans = min(A[1] - A[0], abs(A[0] + K - A[1] + K))

        for i in range(2, len(A)):
            n1 = min(A[i] - A[0], abs(A[0] + K - A[i] + K))
            n2 = min(A[i] - A[i - 1], abs(A[i - 1] + K - A[i] + K))
            ans = max(n1, n2)
        return ans


s = Solution()
print(s.smallestRangeII([0,10], 2))
