"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-1 20:12
Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        cnt = numRows - 2
        while cnt:
            t = [1]
            for i in range(len(ans[-1]) - 1):
                t.append(ans[-1][i] + ans[-1][i + 1])
            t.append(1)
            ans.append(t)
            cnt -= 1
        return ans


    def generate2(self, numRows):
        ans = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans


s = Solution()
print(s.generate2(6))
