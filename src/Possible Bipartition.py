"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-12 12:59
"""
import time


class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        [1,2],[2,3],[3,4],[4,5],[1,5]
        """
        if not dislikes:
            return True
        dic = {}
        for item in dislikes:
            if item[0] not in dic:
                dic[item[0]] = {item[1]: 0}
            else:
                dic[item[0]][item[1]] = 0

        #
        def DFS(targetmap, key, length):
            if key not in dic:
                return True
            if key in dic:
                for e in dic[key]:
                    if e in targetmap:
                        if length % 2 == 1:
                            return False
                    if not DFS(targetmap, e, length + 1):
                        return False
            return True

        for i in range(N):
            if i + 1 not in dic:
                continue
            if not DFS(dic[i + 1], i + 1, 0):
                return False
        return True

    def possibleBipartition2(self, N, dislikes):
        bag = [[] for i in range(N + 1)]
        visited = [-1] * (N + 1)
        count = 0
        for dislike in dislikes:
            bag[dislike[0]].append(dislike[1])
            bag[dislike[1]].append(dislike[0])

        for i in range(1, N + 1):
            if len(bag[i]) > 0:
                break

        return self.visit(0, i, bag, visited)

    def visit(self, curLevel, i, bag, visited):
        if visited[i] >= 0:
            return (curLevel - visited[i]) % 2 == 0

        visited[i] = curLevel
        for des in bag[i]:
            if not self.visit(curLevel + 1, des, bag, visited):
                return False
        return True


s = Solution()
print(time.time())
print(s.possibleBipartition2(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
print(time.time())
