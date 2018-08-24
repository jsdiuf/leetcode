"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-24 17:15
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
 where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = dict()
        for idx, val in enumerate(numbers):
            if target - val in mp:
                return [mp[target - val], idx + 1]
            mp[val] = idx + 1

        """ where is BS（Binary Search）？？？？ fuck！！
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        """



s = Solution()
print(s.twoSum([2, 4, 4, 7, 11, 15], 11))
