"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-1 11:11
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        bigest, secbigest, ans, cnt = nums[0], -1 << 32, 0, 0
        for i, x in enumerate(nums):
            if x == bigest:
                cnt += 1
            if x > bigest:
                ans = i
                cnt = 1
                bigest = x
        if cnt > 1 and bigest != 0:
            return -1
        if bigest == 0:
            return ans

        for i, x in enumerate(nums):
            if x == bigest:
                continue
            if x > secbigest:
                secbigest = x

        return -1 if bigest < secbigest * 2 else ans

        """
        int max = -1, index = -1, second = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > max) {
                second = max;
                max = nums[i];
                index = i;
            } else if (nums[i] > second)
                second = nums[i];
        }
        return second * 2 <= max ? index : -1;
        """


s = Solution()
print(s.dominantIndex([0,0,0,1]))
