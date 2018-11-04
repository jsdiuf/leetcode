"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-4 9:59
A chess knight can move as indicated in the chess diagram below:

 .



This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.



Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46


Note:

1 <= N <= 5000
"""


class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10
        ans = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        ansp = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        for i in range(N - 1):
            ans[1] = ansp[6] + ansp[8]
            ans[2] = ansp[7] + ansp[9]
            ans[3] = ansp[4] + ansp[8]
            ans[4] = ansp[0] + ansp[3] + ansp[9]
            ans[6] = ansp[0] + ansp[1] + ansp[7]
            ans[7] = ansp[2] + ansp[6]
            ans[8] = ansp[1] + ansp[3]
            ans[9] = ansp[2] + ansp[4]
            ans[0] = ansp[4] + ansp[6]
            for i in ansp:
                ansp[i] = ans[i]
        res = 0
        for k in ans:
            res += ans[k]
        return res % (10 ** 9 + 7)


s = Solution()
print(s.knightDialer(4))
