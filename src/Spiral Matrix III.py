"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-12 9:55
"""


class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ret = [[r0, c0]]
        step = 1

        def valid(r0, c0):
            return r0 >= 0 and r0 < R and c0 >= 0 and c0 < C

        while len(ret) < R * C:

            for i in range(step):
                c0 += 1
                if valid(r0, c0):
                    ret.append([r0, c0])

            for i in range(step):
                r0 += 1
                if valid(r0, c0):
                    ret.append([r0, c0])

            step += 1

            for i in range(step):
                c0 -= 1
                if valid(r0, c0):
                    ret.append([r0, c0])

            for i in range(step):
                r0 -= 1
                if valid(r0, c0):
                    ret.append([r0, c0])

            step += 1
        return ret


s = Solution()
print(s.spiralMatrixIII(5, 6, 1, 4))
