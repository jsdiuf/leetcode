"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-2 9:32
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if len(A) == 1:
            return True

        dz, dj = False, False

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                dz = True
            if A[i] < A[i - 1]:
                dj = True
            if dz and dj:
                return False
        return True


s = Solution()
print(s.isMonotonic([2,1, 1,1,1,2]))
