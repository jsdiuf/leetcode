"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-6 13:57
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        pre = [1, 1]
        curr = []

        while rowIndex > 1:
            curr = [1]
            for i in range(len(pre)-1):
                curr.append(pre[i] + pre[i + 1])
            curr.append(1)
            pre = curr
            rowIndex -= 1
        return curr


s=Solution()
print(s.getRow(6))
