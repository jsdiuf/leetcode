"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 0:16
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        for e in nums:
            if e in a:
                a.remove(e)
            else:
                a.add(e)
        return a.pop()


    def singleNumber2(self, nums):
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
        return nums[i]


s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))
