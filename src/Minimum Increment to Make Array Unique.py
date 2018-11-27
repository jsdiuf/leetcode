"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-26 9:36
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.



Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Note:

0 <= A.length <= 40000
0 <= A[i] < 40000
"""


class Solution:
    # TLE
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        ans = 0
        A.sort()
        map = {}
        dis = []

        for i in A:
            if i not in map:
                map[i] = 1
                dis.append(i)
            else:
                map[i] += 1
        for v in dis:
            if map[v] == 1:
                continue
            add = 1
            while map[v] > 1:
                if v + add not in map:
                    map[v + add] = 1
                    map[v] -= 1
                    ans += add
                add += 1
        return ans

        # print(dis)
        # print(map)


    def minIncrementForUnique2(self, A):

        # 1 1 2 2 3 7
        A.sort()
        ans = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                ans += A[i - 1] + 1 - A[i]
                A[i] = A[i - 1] + 1
        return ans


s = Solution()
print(s.minIncrementForUnique2([3, 2, 1, 2, 1, 7]))
