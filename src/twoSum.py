"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 10:38
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for idx, val in enumerate(nums):
            if target - val in dic:
                return [dic[target - val], idx]
            dic[val] = idx
