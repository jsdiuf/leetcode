"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-5 9:05
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max, currMax = 0, 0
        for i in nums:
            if i == 1:
                currMax += 1
            else:
                Max = max(Max, currMax)
                currMax = 0
        return max(Max, currMax)

    """
    return max([len(i) for i in bytearray(nums).split(b'\x00')])
    """


s = Solution()
print(s.findMaxConsecutiveOnes([1,0,0,1,1,1]))
