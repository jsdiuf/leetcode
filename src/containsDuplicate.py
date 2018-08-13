"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-14 0:07
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=set()
        for e in nums:
            if e in a:
                return True
            a.add(e)
        return False

s=Solution()
print(s.containsDuplicate([1,2,3,1]))


