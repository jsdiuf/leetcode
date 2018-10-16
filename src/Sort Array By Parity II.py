"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-14 9:32
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []  # j
        ev = []  # o
        for i in range(len(A)):
            if A[i] & 1 == 0:
                odd.append(A[i])
            else:
                ev.append(A[i])
        ans = []
        for i in range(len(odd)):
            ans.append(odd[i])
            ans.append(ev[i])
        return ans


s = Solution()
print(s.sortArrayByParityII([4, 2, 5, 7]))
