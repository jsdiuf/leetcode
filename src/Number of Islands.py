"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-7 23:11
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col, n = len(grid), len(grid[0]), 0
        color = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]

        def dfs(i, j):
            color[i][j] = n
            if i > 0 and grid[i - 1][j] == '1' and not color[i - 1][j]:  # top
                color[i - 1][j] = n
                dfs(i - 1, j)
            if j > 0 and grid[i][j - 1] == '1' and not color[i][j - 1]:  # left
                color[i][j - 1] = n
                dfs(i, j - 1)
            if i < row - 1 and grid[i + 1][j] == '1' and not color[i + 1][j]:  # bottom
                color[i + 1][j] = n
                dfs(i + 1, j)
            if j < col - 1 and grid[i][j + 1] == '1' and not color[i][j + 1]:  # right
                color[i][j + 1] = n
                dfs(i, j + 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not color[i][j]:
                    n += 1
                    dfs(i, j)
        return n
        """  no need extra space
        private int n;
        private int m;
        
        public int numIslands(char[][] grid) {
            int count = 0;
            n = grid.length;
            if (n == 0) return 0;
            m = grid[0].length;
            for (int i = 0; i < n; i++){
                for (int j = 0; j < m; j++)
                    if (grid[i][j] == '1') {
                        DFSMarking(grid, i, j);
                        ++count;
                    }
            }    
            return count;
        }
        
        private void DFSMarking(char[][] grid, int i, int j) {
            if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != '1') return;
            grid[i][j] = '0';
            DFSMarking(grid, i + 1, j);
            DFSMarking(grid, i - 1, j);
            DFSMarking(grid, i, j + 1);
            DFSMarking(grid, i, j - 1);
        }
        """

s = Solution()
print(s.numIslands([
    ['1', 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]))
