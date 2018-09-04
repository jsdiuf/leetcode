"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-3 22:45
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[nums[0]]]

        ans = self.permute(nums[:-1])

        ret = []

        for item in ans:
            for i in range(len(item)):
                ret.append(item[:i] + [nums[-1]] + item[i:])
            ret.append(item + [nums[-1]])
        return ret


s = Solution()
r = s.permute([1, 2, 3, 4, 5])
print(r)
print(len(r))
