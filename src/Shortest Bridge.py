"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-4 11:51
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)



Example 1:

Input: [[0,1],
       [1,0]]
Output: 1
Example 2:

Input: [[0,1,0],
        [0,0,0],
        [0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]
Output: 1

[[0,1,0,0,0]
,[0,1,0,1,1]
,[0,0,0,0,1]
,[0,0,0,0,0]
,[0,0,0,0,0]]


Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""


class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        s, s1 = set(), set()
        isfirt = False
        r, c = 0, 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    s.add(str(i) + "," + str(j))
                    if not isfirt:
                        r, c = i, j

        def bfs(r, c):
            if r >= 0 and r < len(A) and c >= 0 and c < len(A) and str(r) + "," + str(c) not in s1 and A[r][c] == 1:
                s1.add(str(r) + "," + str(c))
                bfs(r - 1, c)
                bfs(r + 1, c)
                bfs(r, c - 1)
                bfs(r, c + 1)

        bfs(r, c)

        ans = [200]
        visited = set()

        def helper(r, c, step, ans):
            rc = str(r) + "," + str(c)
            if rc not in s1 and rc in s:
                ans[0] = min(ans[0], step)
                return
            visited.add(rc)
            if r - 1 >= 0 and str(r - 1) + "," + str(c) not in visited:
                helper(r - 1, c, step + 1, ans)
            if r + 1 < len(A) and str(r + 1) + "," + str(c) not in visited:
                helper(r + 1, c, step + 1, ans)
            if c - 1 >= 0 and str(r) + "," + str(c - 1) not in visited:
                helper(r, c - 1, step + 1, ans)
            if c + 1 < len(A) and str(r) + "," + str(c + 1) not in visited:
                helper(r, c + 1, step + 1, ans)

        for e in s1:
            e = e.split(",")
            visited.clear()
            helper(int(e[0]), int(e[1]), 0, ans)
        return ans[0]-1


s = Solution()
print(s.shortestBridge([[0,1,0,0,0]
,[0,1,0,1,1]
,[0,0,0,0,1]
,[0,0,0,0,0]
,[0,0,0,0,0]]))
