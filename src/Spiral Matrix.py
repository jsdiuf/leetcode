"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-1 16:53
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        i, j, row, col = 0, 0, len(matrix), len(matrix[0])
        left, right, bottom, top = 0, col - 1, row - 1, 0  # right bottom left top
        move = [1, 0, 0, 0]  # right bottom left top
        ans = []
        for n in range(row * col):
            ans.append(matrix[i][j])
            if move[0]:
                if j < right:
                    j += 1
                else:
                    move[0] = 0
                    move[1] = 1
                    top += 1
            if move[1]:
                if i < bottom:
                    i += 1
                else:
                    move[1] = 0
                    move[2] = 1
                    right -= 1
            if move[2]:
                if j > left:
                    j -= 1
                else:
                    move[2] = 0
                    move[3] = 1
                    bottom -= 1
            if move[3]:
                if i > top:
                    i -= 1
                else:
                    move[3] = 0
                    move[0] = 1
                    left += 1
                    j += 1
        return ans


s = Solution()
print(s.spiralOrder([
    [1],
    [2],
    [3]
]))
