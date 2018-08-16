"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-16 10:57
"""


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = set(J)
        ret = 0
        for e in S:
            if e in s:
                ret += 1
        return ret


s = Solution()
print(s.numJewelsInStones("z", "ZZ"))
