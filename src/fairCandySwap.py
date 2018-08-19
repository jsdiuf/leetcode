"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-19 18:30
"""


class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sa = set(A)
        sb = set(B)
        suma = sum(A)
        sumb = sum(B)
        for e in sa:
            if (sumb - suma + 2 * e) / 2 in sb:
                return [e, (sumb - suma + 2 * e) >> 1]


s = Solution()
print(s.fairCandySwap([1,2], [2, 3]))
