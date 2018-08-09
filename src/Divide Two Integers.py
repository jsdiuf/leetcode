"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-6 9:59
"""

import sys


class Solution:

    def divide3(self, dividend, divisor):

        min = -2147483648
        max = 2147483647
        if dividend == min and divisor == -1:
            return max
        # m/n
        m, n, result = abs(dividend), abs(divisor), 0
        while m >= n:
            s = n
            t = 1
            while s << 1 < m:
                s <<= 1
                t <<= 1
            m -= s
            result += t
        return result if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -result

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        min = -2147483648
        max = 2147483647
        if dividend == min and divisor == -1:
            return max
        ret = dividend // divisor
        ys = dividend % divisor
        if ys == 0:
            return ret
        else:
            if ret < 0:
                return ret + 1
            else:
                return ret


s = Solution()
print(s.divide3(0, 7))
