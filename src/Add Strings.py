"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-11-1 10:01
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        123
           +
       4567
        """

        p1, p2 = len(num1) - 1, len(num2)  - 1
        carry = 0
        ans = ""
        while carry or p1 >= 0 or p2 >= 0:
            s1 = int(num1[p1]) if p1 >= 0 else 0
            s2 = int(num2[p2]) if p2 >= 0 else 0
            s = s1 + s2 + carry
            ans += str(s % 10)
            carry = s // 10
            p1 -= 1
            p2 -= 1
        return ans[::-1]


s = Solution()
print(s.addStrings("2421", "9423434"))
