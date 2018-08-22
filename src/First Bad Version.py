"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-22 16:14
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if not isBadVersion(mid - 1) and isBadVersion(mid):
                return mid
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = (l + r) / 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
