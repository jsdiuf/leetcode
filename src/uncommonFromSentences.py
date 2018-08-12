"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-12 9:31
"""


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        aarr = A.split(" ")
        barr = B.split(" ")

        d1 = {}
        d2 = {}
        ret = []

        for item in aarr:
            if item not in d1:
                d1[item] = 1
            else:
                d1[item] += 1
        for item in barr:
            if item not in d2:
                d2[item] = 1
            else:
                d2[item] += 1

        for e in d1:
            if e not in d2:
                if d1[e] == 1:
                    ret.append(e)
            else:
                del d2[e]
        for item in d2:
            if d2[item] == 1:
                ret.append(item)
        return ret


s = Solution()
print(s.uncommonFromSentences("this apple is sweet", "this apple is sour"))
