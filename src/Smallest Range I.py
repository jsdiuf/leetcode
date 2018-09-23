"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-23 9:33
"""


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        minN = min(A)
        maxN = max(A)

        if maxN - minN <= 2 * K:
            return 0

        return maxN - minN - 2 * K
