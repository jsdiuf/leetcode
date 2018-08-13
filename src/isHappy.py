"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 0:39
"""


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def _next(n):
            ret = 0
            while n > 0:
                r = n % 10
                ret += r ** 2
                n = n // 10
            return ret

        s = set()
        s.add(n)
        while 1:
            n = _next(n)
            if n == 1:
                return True
            if n in s:
                return False
            s.add(n)


s = Solution()
print(s.isHappy(2))
