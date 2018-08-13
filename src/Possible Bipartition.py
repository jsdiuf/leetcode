"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-12 12:59
"""
import collections
import time


class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        [1,2],[2,3],[3,4],[4,5],[1,5]
        [1, 2], [1, 3], [2,4]
        """
        if not dislikes:
            return True
        bag = [[] for i in range(0, N + 1)]
        for item in dislikes:
            bag[item[0]].append(item[1])
            bag[item[1]].append(item[0])
        dept = [-1] * (N + 1)

        def dfs(n, l):
            if dept[n] != -1:
                return (dept[n] - l) % 2 == 0
            dept[n] = l
            for e in bag[n]:
                if not dfs(e, l + 1):
                    return False
            return True
        for idx, val in enumerate(bag):
            if dept[idx] != -1 or not val:
                continue
            if not dfs(idx, 0):
                return False
        return True


s = Solution()
print(time.time())
print(s.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
print(time.time())
