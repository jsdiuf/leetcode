"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-14 9:53
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.



Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 3) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""


class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        map = {}
        dis = []
        for e in A:
            if e not in map:
                map[e] = 1
                dis.append(e)
            else:
                map[e] += 1
        dis.sort()
        ans = 0
        for i in range(len(dis)):
            for j in range(i + 1, len(dis)):
                need = target - dis[i] - dis[j]
                if need in map and (need > dis[j] or need == dis[i] or need == dis[j]):
                    if need != dis[i] and need != dis[j]:
                        ans += map[dis[i]] * map[dis[j]] * map[need]
                    if need == dis[i] and map[need] > 1:
                        ans += map[need] * (map[need] - 1) * map[dis[j]] // 2
                    if need == dis[j] and map[need] > 1:
                        ans += map[need] * (map[need] - 1) * map[dis[i]] // 2

        if target % 3 == 0 and target // 3 in map and map[target // 3] >= 3:
            n = map[target // 3]
            ans += n * (n - 1) * (n - 2) // 6
        return ans % (10 ** 9 + 7)


s = Solution()
print(s.threeSumMulti([1,1,2,2,2,2], 5))
