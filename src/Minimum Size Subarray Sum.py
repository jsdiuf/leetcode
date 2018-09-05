"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-5 9:16
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        BS
        """
        if not nums:
            return 0
        if nums[0] >= s or nums[-1] >= s:
            return 1
        ans = len(nums) + 1
        sumarr = [nums[0]]

        def helper():
            if sumarr[-1] < s:
                return ans
            i, j = 0, len(sumarr) - 1
            while i <= j:
                m = (i + j) // 2
                num1 = sumarr[-1] - sumarr[m] + nums[m]
                num2 = num1 - nums[m]
                if num1 >= s and num2 < s:
                    return len(sumarr) - m
                if num1 < s:
                    j = m - 1
                else:
                    i = m + 1

        for i in range(1, len(nums)):
            sumarr.append(sumarr[-1] + nums[i])
            curr = helper()
            ans = min(ans, curr)
            if ans == 1:
                return 1
        return ans if ans<=len(nums) else 0

    """ excellent solution
        left, sums = 0, 0
        ans = sys.maxsize
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= s:
                ans = min(ans, i + 1 -left)
                sums -= nums[left]
                left += 1
        return ans if ans != sys.maxsize else 0
    """

    """ java
        public int minSubArrayLen(int s, int[] a) {
          if (a == null || a.length == 0)
            return 0;
          
          int i = 0, j = 0, sum = 0, min = Integer.MAX_VALUE;
          
          while (j < a.length) {
            sum += a[j++];
            
            while (sum >= s) {
              min = Math.min(min, j - i);
              sum -= a[i++];
            }
          }
          
          return min == Integer.MAX_VALUE ? 0 : min;
        }    
    """


s = Solution()
print(s.minSubArrayLen(7, [1,1]))
