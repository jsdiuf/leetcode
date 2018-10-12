"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-27 16:06
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        5,4,3,2,1
        1,2,3,4,5
        5,3,2,1
        5,3,2
        """
        if not nums:
            return 1
        dic = {}
        for e in nums:
            if e <= 0:
                continue
            dic[e] = 1

        index = 1
        while 1:
            if index in dic:
                index += 1
            else:
                return index


s = Solution()
print(s.firstMissingPositive([7, 8, 9, 11, 12]))
