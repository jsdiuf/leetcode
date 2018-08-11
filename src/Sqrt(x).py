"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-11 0:24
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        l, r = 1, x

        while r - l > 1:
            mid = (l + r) // 2
            if mid ** 2 > x:
                r = mid
            else:
                l = mid
        return l


s = Solution()
print(s.mySqrt(9))
