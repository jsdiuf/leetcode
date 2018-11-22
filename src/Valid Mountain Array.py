"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-19 15:35
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
"""


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if not A or len(A) < 3 or A[0] > A[1] or A[-1] > A[-2]:
            return False
        arr = []
        for i in range(1, len(A) - 1):
            if A[i] == A[i - 1] or A[i] == A[i + 1]:
                return False
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                arr.append(A[i])
                if len(arr) > 1:
                    return False
        return True


s = Solution()
print(s.validMountainArray([[0, 1, 2, 1, 2]]))
