"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-1 12:19
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        i, j, line, col = 0, 0, len(matrix), len(matrix[0])
        ans = [matrix[0][0]]
        while not (i == line - 1 and j == col - 1):
            if j < col - 1:
                j += 1
            elif i < line - 1:
                i += 1
            while i <= line - 1 and j >= 0:
                ans.append(matrix[i][j])
                i += 1
                j -= 1
            i -= 1
            j += 1
            if i < line - 1:
                i += 1
            elif j < col - 1:
                j += 1
            else:
                return ans
            while i >= 0 and j <= col - 1:
                ans.append(matrix[i][j])
                i -= 1
                j += 1
            i += 1
            j -= 1
        return ans

    def findDiagonalOrder2(self, matrix):
        if not matrix:
            return []
        row, col, d = len(matrix), len(matrix[0]), 0
        i, j = 0, 0
        patt = [[-1, 1], [1, -1]]
        ans = []
        for n in range(row * col):
            ans.append(matrix[i][j])
            i += patt[d][0]
            j += patt[d][1]

            if i >= row:
                i -= 1
                j += 2
                d = 1 - d
            if j >= col:
                j -= 1
                i += 2
                d = 1 - d
            if i < 0:
                i = 0
                d = 1 - d
            if j < 0:
                j = 0
                d = 1 - d

        return ans


s = Solution()
print(s.findDiagonalOrder2([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]

]))
