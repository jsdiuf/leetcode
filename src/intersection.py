"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 0:26
"""


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        a, b = set(nums1), set(nums2)
        ret = []
        for e in a:
            if e in b:
                ret.append(e)
        return ret

s=Solution()
print(s.intersection([9,4],[9,4,9,8,4]))
