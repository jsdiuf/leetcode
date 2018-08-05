"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-5 9:32
"""


class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = 0
        xlen = len(grid[0])
        ylen = len(grid)

        xmax = [0] * xlen
        ymax = [0] * ylen

        for i in range(ylen):

            for j in range(xlen):
                if grid[i][j] > 0:
                    x += 1
                if grid[i][j] > xmax[j]:
                    xmax[j] = grid[i][j]
                if grid[i][j] > ymax[i]:
                    ymax[i] = grid[i][j]

        for i in xmax:
            x += i
        for i in ymax:
            x += i

        return x


s = Solution()
print(s.projectionArea([[1, 0], [0, 2]]))
