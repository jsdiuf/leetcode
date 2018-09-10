"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-6 16:26
https://leetcode.com/problems/sudoku-solver/description/
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
https://leetcode.com/problems/sudoku-solver/description/
"""
import copy


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        虽然AC 了   但是需要2.6s 而且deepcopy内存用太多了 太扯了 有时间 优化。。。。。
        """
        fix = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    fix += 1
        if fix == 81:
            return

        def helper(i, j, board):
            ans = set(str(i) for i in range(1, 10))
            for col in range(9):
                if board[i][col] != "." and board[i][col] in ans:
                    ans.remove(board[i][col])
            for row in range(9):
                if board[row][j] != "." and board[row][j] in ans:
                    ans.remove(board[row][j])
            row, col = i // 3, j // 3
            for m in range(3 * row, 3 * row + 3):
                for n in range(3 * col, 3 * col + 3):
                    if board[m][n] != "." and board[m][n] in ans:
                        ans.remove(board[m][n])
            return ans

        while fix <= 81:
            change = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        re = helper(i, j, board)
                        if len(re) == 1:
                            board[i][j] = re.pop()
                            fix += 1
                            change = True
            if not change:
                break
        if fix == 81:
            for i in range(9):
                for j in range(9):
                    board[i][j] = str(board[i][j])
            return

        def backtrack(i, j, grid, ans):
            if i == 8 and j == 8:
                if grid[i][j] != ".":
                    ans.append(grid)
                    return
                re = helper(i, j, grid)
                if len(re) >= 1:
                    grid[i][j] = re.pop()
                    ans.append(grid)
                    return
            elif grid[i][j] != ".":
                if j < 8:
                    backtrack(i, j + 1, grid, ans)
                else:
                    backtrack(i + 1, 0, grid, ans)
            else:
                re = helper(i, j, grid)
                if not re:  # 前面尝试失败
                    return
                while re:
                    grid[i][j] = re.pop()
                    backtrack(i, j + 1, copy.deepcopy(grid), ans) if j < 8 else backtrack(i + 1, 0, copy.deepcopy(grid),
                                                                                          ans)

        ans = []
        backtrack(0, 0, copy.deepcopy(board), ans)
        # print(ans)
        # board = ans[0]
        for i in range(9):
            for j in range(9):
                board[i][j] = ans[0][i][j]


s = Solution()
a = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
     ["7", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", "2", ".", "1", ".", "9", ".", ".", "."],
     [".", ".", "7", ".", ".", ".", "2", "4", "."],
     [".", "6", "4", ".", "1", ".", "5", "9", "."],
     [".", "9", "8", ".", ".", ".", "3", ".", "."],
     [".", ".", ".", "8", ".", "3", ".", "2", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "6"],
     [".", ".", ".", "2", "7", "5", "9", ".", "."]]
s.solveSudoku(a)
print(a)
