"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-22 17:34

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        7,8,9,0,1,2,3,4,5,6
        3,4,5,6,7,8,9,0,1,2
        """
        if not nums:
            return None
        if nums[-1] >= nums[0]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                if nums[m + 1] < nums[m]:
                    return nums[m + 1]
                l = m + 1
            else:
                if nums[m] < nums[m - 1]:
                    return nums[m]
                r = m - 1

    """
     int findMin(vector<int> &num) {
        int start=0,end=num.size()-1;
        
        while (start<end) {
            if (num[start]<num[end])
                return num[start];
            
            int mid = (start+end)/2;
            
            if (num[mid]>=num[start]) {
                start = mid+1;
            } else {
                end = mid;
            }
        }
        
        return num[start];
    }
    """



s = Solution()
print(s.findMin([4,3,-1,0,1,2]))
