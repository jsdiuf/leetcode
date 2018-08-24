"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-24 9:14
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1 / x

        ans = 1
        tn = 1
        tx = x
        while n > 0:
            if tn < n:
                ans *= tx
                tx *= tx
                n -= tn
                tn *= 2
            else:
                ans *= x
                tx = x
                tn = 1
                n -= 1
        return round(ans, 5)

    # clever
    def myPow2(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        return self.myPow2(x * x, n / 2) if n % 2 == 0 else x * self.myPow2(x * x, n / 2)


s = Solution()
print(s.myPow(2, 500))
