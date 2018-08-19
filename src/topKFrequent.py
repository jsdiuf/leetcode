"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-17 22:16
"""
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = Counter(nums)
        l = [[d[e], e] for e in d]
        l = sorted(l, key=lambda l: -l[0])
        ret = []
        for i in range(k):
            ret.append(l[i][1])
        return ret

    # bucket sort 这样桶里面得是数组 防止两个数个数一样覆盖的情况
    def topKFrequent2(self, nums, k):
        d = Counter(nums)
        bucket = [0] * len(nums)
        for e in d:
            bucket[d[e]] = e
        ret = []
        for i in range(len(nums) - 1, 0, -1):
            if bucket[i] != 0:
                ret.append(bucket[i])
                k -= 1
                if k == 0:
                    return ret


s = Solution()
print(s.topKFrequent2([1, 1, 1, 2, 2,2, 3], 2))
