"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-17 21:57
"""


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic1 = {}
        dic2 = {}
        if not A:
            return 0
        for i in A:
            for j in B:
                if (i + j) not in dic1:
                    dic1[i + j] = 1
                else:
                    dic1[i + j] += 1
        for i in C:
            for j in D:
                if (i + j) not in dic2:
                    dic2[i + j] = 1
                else:
                    dic2[i + j] += 1
        res = 0
        for e in dic1:
            if (0 - e) in dic2:
                res += dic1[e] * dic2[0 - e]
        return res


s=Solution()
print(s.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))