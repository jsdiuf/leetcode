"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-15 10:07
"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1, dic2 = {}, {}
        ret = []
        for e in nums1:
            dic1[e] = 1 if e not in dic1 else dic1[e] + 1
        for e in nums2:
            dic2[e] = 1 if e not in dic2 else dic2[e] + 1
        for e in dic1:
            if e in dic2:
                ret.extend([e] * min(dic1[e], dic2[e]))
        return ret


s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
