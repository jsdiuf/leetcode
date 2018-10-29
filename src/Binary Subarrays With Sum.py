"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-29 9:36
In an array A of 0s and 1s, how many non-empty subarrays have sum S?



Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""
from collections import defaultdict


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        100100
        """
        arr = []
        ans = 0
        for i in range(len(A)):
            if A[i] == 1:
                arr.append(i)

        if len(arr) < S:
            return 0

        def helper(i):
            return (1 + i) * i // 2

        if S == 0:
            if not arr:
                return helper(len(A))
            ans += helper(arr[0])
            for i in range(1, len(arr)):
                ans += helper(arr[i] - arr[i - 1] - 1)
            ans += helper(len(A) - arr[-1] - 1)
            return ans

        i, j = 0, S - 1

        while j < len(arr):
            l = arr[0] if i == 0 else arr[i] - arr[i - 1] - 1
            r = len(A) - arr[-1] - 1 if j == len(arr) - 1 else arr[j + 1] - arr[j] - 1
            ans += (l + 1) * (r + 1)
            i += 1
            j += 1
        return ans

    def numSubarraysWithSum2(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        d=defaultdict(lambda:0)
        ps=0
        ans=0
        for a in A:
            d[ps]+=1
            ps+=a
            ans+=d[ps-S]
        return ans


s = Solution()
print(s.numSubarraysWithSum([0, 0, 0,0,0, 0], 0))
