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
        dic = {}
        for item in dislikes:
            if item[0] not in dic:
                s = set()
                s.add(item[1])
                dic[item[0]] = s
            else:
                dic[item[0]].add(item[1])
        color = [-1] * (N + 1)

        left = set()
        right = set()
        putl = True
        for e in dic:
            if not left and not right:
                left.add(e)
                right = dic[e]
            if putl:
                for i in dic[e]:
                    if i in left:
                        return False
                    left.add(i)
            if not putl:
                for i in dic[e]:
                    pass

    def possibleBipartition2(self, N, dislikes):
        bag = [[] for i in range(N + 1)]
        visited = [-1] * (N + 1)

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

    def possibleBipartition3(self, N, dislikes):
        edges = [[]] * N
        for pair in dislikes:
            edges[pair[0] - 1].append(pair[1] - 1)
            edges[pair[1] - 1].append(pair[0] - 1)

        team = [-1] * N
        for i, p in enumerate(team):
            if p == -1:
                team[i] = 0
                q = collections.deque()
                q.append(i)
                while len(q):
                    pre = q.popleft()
                    for j in edges[pre]:
                        if team[j] == -1:
                            team[j] = 1 - team[pre]
                            q.append(j)
                        elif team[j] == team[pre]:
                            return False
        return True


s = Solution()
print(time.time())
print(s.possibleBipartition3(15, [[1, 2], [1, 3], [10, 11], [11, 12], [10, 12]]))
print(time.time())
