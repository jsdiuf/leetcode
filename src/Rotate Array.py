"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-5 16:19
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        [1,2,3,4,5,6]
        [5,6,1,2,3,4]
        """
        if not nums:
            return
        k = k % len(nums)
        nums[:k], nums[k:] = nums[-k:], nums[:len(nums) - k]
        print(nums)


    """ excellent solution
      public void rotate(int[] nums, int k) {
          k %= nums.length;
          reverse(nums, 0, nums.length - 1);
          reverse(nums, 0, k - 1);
          reverse(nums, k, nums.length - 1);
      }
      
      public void reverse(int[] nums, int start, int end) {
          while (start < end) {
              int temp = nums[start];
              nums[start] = nums[end];
              nums[end] = temp;
              start++;
              end--;
          }
      }    
    """

s=Solution()
print(s.rotate([1,2,3,4,5,6],5))
