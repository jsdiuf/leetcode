"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-24 10:43
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.
"""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num in [i * i for i in range(5)]:
            return True
        l, r = 1, num // 2
        while l <= r:
            m = (l + r) // 2
            if m * m == num:
                return True
            if m * m < num:
                l = m + 1
            else:
                r = m - 1
        return False


s=Solution()
print(s.isPerfectSquare(18*18+1))
