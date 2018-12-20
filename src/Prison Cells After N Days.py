"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018/12/20 16:00
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)



Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]


Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""


class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        def get_next(arr):
            res = [0]
            for i in range(1, 7):
                res.append(0 if arr[i - 1] ^ arr[i + 1] else 1)
            return res + [0]

        s = set()
        list = []
        cells = get_next(cells)
        s.add(tuple(cells))
        list.append(cells)
        s.add(tuple(cells))
        for i in range(N - 1):
            cells = get_next(cells)
            if tuple(cells) in s:
                return list[(N - 1) % len(list)]
            s.add(tuple(cells))
            list.append(cells)
        return list[-1]


s = Solution()
print(s.prisonAfterNDays([0, 0, 1, 0, 0, 1, 0, 0], 44640906))
