"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-26 15:20
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""


class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0

        def getbefore(i, j):
            if i == 0:
                return grid[i][j]
            ret = grid[i][j] - grid[i - 1][j]
            return ret if ret > 0 else 0

        def getafter(i, j):
            if i == len(grid) - 1:
                return grid[i][j]
            ret = grid[i][j] - grid[i + 1][j]
            return ret if ret > 0 else 0

        def getleft(i, j):
            if j == 0:
                return grid[i][j]
            ret = grid[i][j] - grid[i][j - 1]
            return ret if ret > 0 else 0

        def getright(i, j):
            if j == len(grid[0]) - 1:
                return grid[i][j]
            ret = grid[i][j] - grid[i][j + 1]
            return ret if ret > 0 else 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                ans += getbefore(i, j)
                ans += getafter(i, j)
                ans += getleft(i, j)
                ans += getright(i, j)
                ans += 2
        return ans

s=Solution()
print(s.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))
