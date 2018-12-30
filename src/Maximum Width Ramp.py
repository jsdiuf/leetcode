"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018/12/23 10:38
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.


Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000

"""


class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = [[A[0], 0]]
        ans = 0

        def insert(index):
            if s[-1][0] < A[index]:
                s.append([A[index], index])
                return
            for i in range(len(s)):
                if s[i][0] > A[index]:
                    s.insert(i, [A[index], index])
                    return

        def getn(index):

            i = 0
            ret = 0
            while i < len(s) and s[i][0] <= A[index]:
                ret = max(ret, index - s[i][1])
                i += 1
            return ret

        for i in range(1, len(A)):
            t = getn(i)
            ans = max(t, ans)
            insert(i)

        t = getn(len(A) - 1)
        ans = max(t, ans)

        return ans

    # nice
    def maxWidthRamp2(self, A):
        table = [(a, i) for i, a in enumerate(A)]
        table.sort()

        imin = float('Inf')
        res = 0
        for a, i in table:
            res = max(res, i - imin)
            imin = min(imin, i)

        return res


s = Solution()
print(s.maxWidthRamp2([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))