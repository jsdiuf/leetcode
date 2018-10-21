"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-21 12:38
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.



Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.


    "0101100011"
Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""


class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        len_0, len_1 = 0, 0
        S = list(S)
        for i in range(len(S)):
            if S[i] == '0':
                len_0 += 1
            if S[i] == '1':
                len_1 += 1
        ans = min(len_0, len_1)
        if ans == 0:
            return 0
        b_0 = 0
        b_1 = 0
        for i in range(len(S)):
            if S[i] == '0':
                ans = min(ans, b_1 + len_0 - 1 - b_0)
                b_0 += 1
            else:
                ans = min(ans, b_1 + len_0 - b_0)
                b_1 += 1
        return ans


s = Solution()
print(s.minFlipsMonoIncr("00011000"))
