"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 16:52
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def judge(list):
            s = set()
            for i in list:
                if i != "." and i in s:
                    return False
                s.add(i)
            return True

        # every line
        for e in board:
            if not judge(e):
                return False
        # every column
        for i in range(9):
            list = []
            for j in range(9):
                list.append(board[j][i])
            if not judge(list):
                return False
        # every square
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                list = []
                list.extend(board[i][j:j + 3])
                list.extend(board[i + 1][j:j + 3])
                list.extend(board[i + 2][j:j + 3])
                if not judge(list):
                  return False
        return True

s=Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))